//var React = require('react')
//var ReactDom = require('react-dom')
//
//ReactDom.render(
//    <h1>hello world</h1>, 
//    document.getElementById('app')
//);
//
var Helloworld = React.createClass({
    render:function(){
    return (
        <div className = "test">
            God Damn
        </div>
        )
    }
});

React.render(
    <Helloworld />,
    document.getElementById("first")
);