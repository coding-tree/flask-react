import React from "react";
import { Route, BrowserRouter as Router } from "react-router-dom";
import "./template/assets/css/wr.css";
import "./template/assets/vendor/nucleo/css/nucleo.css";

import { Home, Profile, Login, Register, Tickets } from "./components";

function App() {
  return (
    <div className="App">
      <Router>
        <Route exact path="/" component={Home} />
        <Route exact path="/profile" component={Profile} />
        <Route path="/login" component={Login} />
        <Route path="/register" component={Register} />
        <Route path="/tickets" component={Tickets} />
      </Router>
    </div>
  );
}

export default App;
