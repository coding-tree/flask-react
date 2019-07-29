import React from "react";
import { Link } from "react-router-dom";

import "../template/assets/css/wr.css";
import "../template/assets/vendor/nucleo/css/nucleo.css";

import facebook from "../template/assets/img/icons/common/facebook.svg";
import google from "../template/assets/img/icons/common/google.svg";

function Login() {
  
  const loginUser = () => {
    console.log("Login handler function", "CLICKED");

    fetch("/api/login", {
      headers: {
        "Content-Type": "application/Json"
      },
      method: "POST",
      body: JSON.stringify(user)
    })
      .then(response => response.json())
      .then(responseJson => {
        var response = responseJson;
        console.log(response);
      });
  };

  return (
    <div>
      <header className="header-global">
        <nav
          id="navbar-main"
          className="navbar navbar-main navbar-expand-lg navbar-transparent navbar-light headroom"
        >
          <div className="container">
            LOGO
            <button
              className="navbar-toggler"
              type="button"
              data-toggle="collapse"
              data-target="#navbar_global"
              aria-controls="navbar_global"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon" />
            </button>
            <div className="navbar-collapse collapse" id="navbar_global">
              <div className="navbar-collapse-header">
                <div className="row">
                  <div className="col-6 collapse-brand">
                    <a href="home">
                      <img src="" alt="logo" />
                    </a>
                  </div>
                  <div className="col-6 collapse-close">
                    <button
                      type="button"
                      className="navbar-toggler"
                      data-toggle="collapse"
                      data-target="#navbar_global"
                      aria-controls="navbar_global"
                      aria-expanded="false"
                      aria-label="Toggle navigation"
                    >
                      <span />
                      <span />
                    </button>
                  </div>
                </div>
              </div>
              <ul className="navbar-nav navbar-nav-hover align-items-lg-center">
                <li className="nav-item dropdown">
                  <a
                    href="profile"
                    className="nav-link"
                    data-toggle="dropdown"
                    role="button"
                  >
                    <i className="ni ni-collection d-lg-none" />
                    <span className="nav-link-inner--text">LSD</span>
                  </a>
                  <div className="dropdown-menu">
                    <a href="messages" className="dropdown-item">
                      <i className="fas fa-envelope" />
                      Wiadomości
                    </a>
                    <a href="profile" className="dropdown-item">
                      <i className="fas fa-user-circle" />
                      Profil
                    </a>
                    <a href="logout" className="dropdown-item">
                      <i className="fas fa-door-open" />
                      Wyloguj
                    </a>
                  </div>
                </li>
              </ul>
              <ul className="navbar-nav align-items-lg-center ml-lg-auto">
                <li className="nav-item">
                  <a className="nav-link nav-link-icon" href="forum">
                    <i className="fas fa-comments" />
                    <span className="nav-link-inner--text d-lg-none">
                      Forum
                    </span>
                  </a>
                </li>
                <li className="nav-item">
                  <a className="nav-link nav-link-icon" href="support">
                    <i className="far fa-life-ring" />
                    <span className="nav-link-inner--text d-lg-none">
                      Support
                    </span>
                  </a>
                </li>
                <li className="nav-item">
                  <a className="nav-link nav-link-icon" href="market">
                    <i className="fas fa-shopping-cart" />
                    <span className="nav-link-inner--text d-lg-none">
                      Market
                    </span>
                  </a>
                </li>
                <li className="nav-item">
                  <a className="nav-link nav-link-icon" href="dicord">
                    <i className="fab fa-discord" />
                    <span className="nav-link-inner--text d-lg-none">
                      Discord
                    </span>
                  </a>
                </li>
                <li className="nav-item d-none d-lg-block ml-lg-4">
                  <a href="register" className="btn btn-neutral btn-icon">
                    <span className="btn-inner--icon">
                      <i className="fa fa-user-plus " />
                    </span>
                    <Link className="nav-link-inner--text" to="/register">
                      Rejestracja
                    </Link>
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </nav>
      </header>
      <main>
        <section className="section section-shaped section-lg">
          <div className="shape shape-style-1 bg-gradient-default">
            <span />
            <span />
            <span />
            <span />
            <span />
            <span />
            <span />
            <span />
          </div>
          <div className="container pt-lg-md">
            <div className="row justify-content-center">
              <div className="col-lg-5">
                <div className="card bg-secondary shadow border-0">
                  <div className="card-header bg-white pb-5">
                    <div className="text-muted text-center mb-3">
                      <small>Zaloguj się za pomocą</small>
                    </div>
                    <div className="btn-wrapper text-center">
                      <a href="#" className="btn btn-neutral btn-icon mr-4">
                        <span className="btn-inner--icon">
                          <img src={facebook} />
                        </span>
                        <span className="btn-inner--text">Facebook</span>
                      </a>
                      <a href="#" className="btn btn-neutral btn-icon">
                        <span className="btn-inner--icon">
                          <img src={google} />
                        </span>
                        <span className="btn-inner--text">Google</span>
                      </a>
                    </div>
                  </div>
                  <div className="card-body px-lg-5 py-lg-5">
                    <div className="text-center text-muted mb-4" />
                    <form>
                      <div className="form-group mb-3">
                        <div className="input-group input-group-alternative">
                          <div className="input-group-prepend">
                            <span className="input-group-text">
                              <i className="ni ni-email-83" />
                            </span>
                          </div>
                          <input
                            className="form-control"
                            placeholder="Email"
                            type="email"
                          />
                        </div>
                      </div>
                      <div className="form-group">
                        <div className="input-group input-group-alternative">
                          <div className="input-group-prepend">
                            <span className="input-group-text">
                              <i className="ni ni-lock-circle-open" />
                            </span>
                          </div>
                          <input
                            className="form-control"
                            placeholder="Password"
                            type="password"
                          />
                        </div>
                      </div>
                      <div className="custom-control custom-control-alternative custom-checkbox">
                        <input
                          className="custom-control-input"
                          id=" customCheckLogin"
                          type="checkbox"
                        />
                        <label
                          className="custom-control-label"
                          htmlFor=" customCheckLogin"
                        >
                          <span>Zapamiętaj mnie</span>
                        </label>
                      </div>
                      <div className="text-center">
                        <button
                          type="button"
                          className="btn btn-primary my-4"
                          onClick={loginUser}
                        >
                          Zaloguj
                        </button>
                      </div>
                    </form>
                  </div>
                </div>
                <div className="row mt-3">
                  <div className="col-6">
                    <a href="forgetpassword" className="text-light">
                      <small>Zapomniałeś hasła?</small>
                    </a>
                  </div>
                  <div className="col-6 text-right">
                    <Link className="text-light" to="/register">
                      <small>Zarejestruj się!</small>
                    </Link>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
      </main>
    </div>
  );
}
export default Login;
