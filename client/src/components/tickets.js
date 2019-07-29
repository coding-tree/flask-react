import React from 'react'

function Tickets() {
    return (
        <div>
            <header class="header-global">
          <nav id="navbar-main" class="navbar navbar-main navbar-expand-lg navbar-transparent navbar-light headroom">
            <div class="container">
              LOGO
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbar_global" aria-controls="navbar_global" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="navbar-collapse collapse" id="navbar_global">
          <div class="navbar-collapse-header">
            <div class="row">
              <div class="col-6 collapse-brand">
                <a href="../index.html">
                  <img src="../assets/img/brand/blue.png"/>
                </a>
              </div>
              <div class="col-6 collapse-close">
                <button type="button" class="navbar-toggler" data-toggle="collapse" data-target="#navbar_global" aria-controls="navbar_global" aria-expanded="false" aria-label="Toggle navigation">
                  <span></span>
                  <span></span>
                </button>
              </div>
            </div>
          </div>
          <ul class="navbar-nav navbar-nav-hover align-items-lg-center">
            <li class="nav-item dropdown">
              <a href="#" class="nav-link" data-toggle="dropdown" role="button">
                <i class="ni ni-collection d-lg-none"></i>
                <span class="nav-link-inner--text">LSD</span>
              </a>
              <div class="dropdown-menu">
                <a href="#" class="dropdown-item"><i class="fas fa-envelope"></i>Wiadomości</a>
                <a href="#" class="dropdown-item"><i class="fas fa-user-circle"></i>Profil</a>
                <a href="#" class="dropdown-item"><i class="fas fa-door-open"></i>Wyloguj</a>
              </div>
            </li>
          </ul>
          <ul class="navbar-nav align-items-lg-center ml-lg-auto">
            <li class="nav-item">
              <a class="nav-link nav-link-icon" href="#">
                <i class="fas fa-comments"></i>
                <span class="nav-link-inner--text d-lg-none">Forum</span>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link nav-link-icon" href="#">
                <i class="far fa-life-ring"></i>
                <span class="nav-link-inner--text d-lg-none">Support</span>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link nav-link-icon" href="#">
                <i class="fas fa-shopping-cart"></i>
                <span class="nav-link-inner--text d-lg-none">Market</span>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link nav-link-icon" href="#">
                <i class="fab fa-discord"></i>
                <span class="nav-link-inner--text d-lg-none">Discord</span>
              </a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
  <main class="profile-page">
    <section class="section-profile-cover section-shaped my-0">
      <div class="shape shape-style-1 bg-gradient-default alpha-4">
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
      </div>
      <div class="container shape-container d-flex align-items-center py-lg">
          <div class="col px-4">
            <div class="row align-items-center justify-content-center">
              <div class="col-lg-64 text-center">
                <p class="lead text-white" style={{fontSize:36+'px', marginBottom:150+'px'}}>Twoje zgloszenia.</p>
              </div>
            </div>
          </div>
        </div>
    </section>
    <section class="section">
      <div class="container">
        <div class="card card-profile shadow" style={{marginTop: -250+'px'}}>
          <div class="px-4">
            <div class='table-responsive'>
 <table id="tablePreview" class="table table-hover">
   <thead>
     <tr>
       <th>#</th>
       <th>Temat</th>
       <th>Status</th>
       <th>Data utworzenia</th>
       <th>Ostatnia odpowiedź</th>
       <th></th>
     </tr>
   </thead>
   <tbody>
     <tr>
       <th scope="row">1</th>
       <td>Pomoc</td>
       <td><span class="badge badge-success">Otwarte</span></td>
       <td>27/07/2019</td>
       <td>Mark</td>
       <td>
           <button type="button" class="btn btn-default btn-sm">Podgląd</button>
           <button type="button" class="btn btn-danger btn-sm"><i class="fas fa-edit"></i>Edytuj</button>
       </td>
     </tr>
   </tbody>
 </table>
 <div style={{marginBottom: 10+'px'}}>
 <button type="button" class="btn btn-secondary"><i class="fas fa-plus"/></button>
<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModal">
  Launch demo modal
</button>
<div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        ...
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
 </div>

          </div>
        </div>
      </div>
    </div>
    </section>
  </main>
        </div>
    )
}
export default Tickets