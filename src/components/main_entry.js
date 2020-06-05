import React from "react"

export default (props) => (
    <div id={props.title}>
        <h2>{props.title}</h2>
        <p>{props.text}</p>
    </div>
)
