# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashWebsocket(Component):
    """A DashWebsocket component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- msg (string; optional):
    The websocket response message.

- url (string; optional):
    The url for websocket."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dashwebsocket'
    _type = 'DashWebsocket'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, msg=Component.UNDEFINED, url=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'msg', 'url']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'msg', 'url']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DashWebsocket, self).__init__(**args)
