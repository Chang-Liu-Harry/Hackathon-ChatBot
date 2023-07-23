import React,

{Component}
from

'react';
import axios
from

'axios';


class App extends Component {
constructor() {
super();
this.state = {
message: '',
         conversation: []

};
}

updateMessage = (event) = > {
    this.setState({
        message: event.target.value
    });
}

sendMessage = async () = > {
    const
message = this.state.message;
const
conversation = this.state.conversation;

// Update
conversation
state
conversation.push({role: 'user', text: message});
this.setState({conversation: conversation, message: ''});

// Send
POST
request
to
server
const
response = await axios.post('http://localhost:5000/get_response', {conversation: conversation});

// Update
conversation
state
conversation.push({role: 'bot', text: response.data.response});
this.setState({conversation: conversation});
}

render()
{
    const
conversation = this.state.conversation.map((element, index) = >
< p
key = {index} > < b > {element.role}: < / b > {element.text} < / p >
);

return (
    < div >
    < div > {conversation} < / div >
    < input value={this.state.message} onChange={this.updateMessage} / >
    < button onClick={this.sendMessage} > Send < / button >
    < / div >
);
}
}

export
default
App;