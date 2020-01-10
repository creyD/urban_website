import React from "react"

export default props => (
  <div id={props.title}>
    <h1>{props.title}</h1>
    <p>{props.text}</p>
  </div>
)
