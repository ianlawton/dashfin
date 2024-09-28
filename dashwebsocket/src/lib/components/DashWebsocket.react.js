import React, {Component} from 'react';
import PropTypes from 'prop-types';
// import { w3cwebsocket as W3CWebSocket } from "websocket";
import io from "socket.io-client";

/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */
export default class DashWebsocket extends Component {
    componentDidMount() {
        /*
        const url = this.props.url;
        const client = new W3CWebSocket(url);
        client.onopen = () => {
            console.log('websocket connected');
        }
        client.onmessage = (message) => {
            this.props.setProps({ msg: message.data})
        }*/

        if (window.fin) {
            console.log('OpenFin found');

        }
        else{
            console.log('OpenFin not found')
        }

        if (window.fdc3 !== undefined) {
            console.log('Not undefined');
            this.setupListeners();
        } else {
            console.log('undefined');
            window.addEventListener('fdc3Ready', async () => {
                
                this.setupListeners();
            });
        }

       // const socket = io.connect(this.props.url, { transports: ["websocket", "polling"], upgrade: false});
       // socket.on("receive_message", (data) => {
       //     alert(data.message);
       //     this.props.setProps({ msg: data.message.data})
       //   });

    }

    /**
     * Sets up the related fdc3 listeners once fdc3 is available.
     */
    setupListeners() {
        try {
            console.log('Setting up listeners');
            window.fdc3.addContextListener(this.contextHandler);
            // window.fdc3.addIntentListener('ViewContact', contextHandler);
            // window.fdc3.addIntentListener('ViewProfile', contextHandler);
        } catch (error) {
            console.error('There was an error while setting up all of the fdc3 listeners', error);
        }
    }

    /**
     * Handler for setting the context.
     * @param ctx The FDC3 context.
     */
    contextHandler(ctx) {
        console.log('Context Received:', ctx);
        if (ctx.type === 'fdc3.contact') {
            // setContact(ctx);
        }
    }


    render() {
        const {id, setProps, url, msg} = this.props;

        return (
            <div id={id}>
                <table>
                    <tbody>
                        <tr><td>url</td><td><input defaultValue={url}/></td></tr>
                        <tr><td>msg</td><td><textarea defaultValue={msg}/></td></tr>
                    </tbody>
                </table>
            </div>
        );
    }
}

DashWebsocket.defaultProps = {};

DashWebsocket.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * The websocket response message.
     */
    msg: PropTypes.string,

    /**
     * The url for websocket.
     */    
    url: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
