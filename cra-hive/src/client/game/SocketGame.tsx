import GenericGame from "./GenericGame";
import useForceUpdate from "../utils/useForceUpdate";
import useHiveGame from "./useHiveGame";
import { useEffect } from "react";

export default function SocketGame( {socket, gid, p1, p2} ) {
    const forceUpdate = useForceUpdate();
    const {apply, state} = useHiveGame();
    const submitAction = (action) => socket.emit("intendAction", {action: action})
    useEffect( () => {
        socket.emit('joinGame', gid)
        const actionListener = (action) => {
            apply(action);
            forceUpdate();
        }
        socket.on('updateAction', actionListener)
        return () => {
            socket.off('updateAction', actionListener)
        }
    }, [socket])
    return <Wrapped state={state} p1={p1} p2={p2} submitAction={submitAction} />
}    

function Wrapped({state, p1, p2, submitAction}) {
    const player = ((state.turnNumber % 2 === 0) ? p1 : p2)(submitAction, state)
    return (
        <GenericGame controller={player} state={state} />
    )
}
