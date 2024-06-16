import React, { useState, ReactNode, isValidElement } from "react";

function getNodeContent(node: ReactNode): string {

    /**
     * a possible bug here:
     * maybe a graph is truncated
     */
    if(node == undefined) return ""
    if (['string', 'number', 'boolean'].includes(typeof node)) return node?.toLocaleString()
    if (node instanceof Array) return node.find(x => typeof x === 'string')
    if (isValidElement(node)) return getNodeContent(node.props.children)

    console.error(`unknown node: ${node}`)
    return ""
}

export default function CollapsibleChatItem({ node }: { node: ReactNode }) {

    console.log('node', node)

    const nodeContent = getNodeContent(node)
    console.log('node content', nodeContent)

    const [open, setOpen] = useState(nodeContent.length <= 80)

    return (
        <>
            {open ? node : (<>hello {nodeContent.substring(0, 8)}</>)}
        </>
    );
}