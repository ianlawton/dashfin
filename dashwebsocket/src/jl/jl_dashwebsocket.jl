# AUTO GENERATED FILE - DO NOT EDIT

export jl_dashwebsocket

"""
    jl_dashwebsocket(;kwargs...)

A DashWebsocket component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `msg` (String; optional): The websocket response message.
- `url` (String; optional): The url for websocket.
"""
function jl_dashwebsocket(; kwargs...)
        available_props = Symbol[:id, :msg, :url]
        wild_props = Symbol[]
        return Component("jl_dashwebsocket", "DashWebsocket", "dashwebsocket", available_props, wild_props; kwargs...)
end

