document.addEventListener('DOMContentLoaded', function() {
  const menuIcon = document.querySelector('.menu-icon');
  const navList = document.querySelector('nav ul');
  const body = document.body;
  const menuItems = document.querySelectorAll('nav ul li a');

  menuIcon.addEventListener('click', function() {
    navList.classList.toggle('show');
    body.classList.toggle('show-menu');
  });

  // Ajouter un gestionnaire d'événements pour chaque élément du menu
  menuItems.forEach(function(menuItem) {
    menuItem.addEventListener('click', function(event) {
      // Empêcher le comportement par défaut du lien
      event.preventDefault();

      // Récupérer l'ID de la cible à partir de l'attribut href du lien
      const targetId = this.getAttribute('href').substring(1);
      const targetElement = document.getElementById(targetId);

      // Vérifier si l'élément cible existe
      if (targetElement) {
        // Effectuer le défilement fluide vers l'élément cible
        targetElement.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });

        // Fermer le menu (si nécessaire)
        navList.classList.remove('show');
        body.classList.remove('show-menu');
      }
    });
  });
});


// let brevetBtn = document.getElementById('brevetBtn');
// let bacBtn = document.getElementById('bacBtn');

// let brevetContent = document.getElementById('brevetContent');
// let bacContent = document.getElementById('bacContent');

// let proposmoibtn = document.getElementById('proposmoibtn');
// let proposmoip = document.getElementById('proposmoip');

let stageeffseit = document.getElementById('stageeffseit');
let stageeffseittexte = document.getElementById('stageeffseittexte');
let stageeffseitBtn = document.getElementById('stageeffseitBtn');

let stageiyoo = document.getElementById('stageiyoo');
let stageiyootexte = document.getElementById('stageiyootexte');
let stageiyooBtn = document.getElementById('stageiyooBtn');

// let stagetennis = document.getElementById('stagetennis');
// let stagetennistexte = document.getElementById('stagetennistexte');

// let stagecpam = document.getElementById('stagecpam');
// let stagecpamtexte = document.getElementById('stagecpamtexte');

//diplome//
// brevetBtn.addEventListener('mouseover', function () {
//   brevetContent.style.color = '#ffffff';
// });

// brevetBtn.addEventListener('mouseout', function () {
//   brevetContent.style.color = 'transparent';
// });

// bacBtn.addEventListener('mouseover', function () {
//   bacContent.style.color = '#ffffff';
// });

// bacBtn.addEventListener('mouseout', function () {
//   bacContent.style.color = 'transparent';
// });

//mon parcours//
// proposmoibtn.addEventListener('mouseover', function () {
//   proposmoip.style.color = '#ffffff';
// });

// proposmoibtn.addEventListener('mouseout', function () {
//   proposmoip.style.color = 'transparent';
// });


//stages//
stageeffseit.addEventListener('click', function () {
  stageeffseittexte.style.display = 'block';
  stageeffseitBtn.style.display = 'block';
  stageiyootexte.style.display = 'none';
  stageiyooBtn.style.display = 'none';
  // stagetennistexte.style.color = 'transparent';
  // stagecpamtexte.style.color = 'transparent';

  stageeffseit.style.backgroundColor = '#dedede';
  stageiyoo.style.backgroundColor = 'transparent';
  // stagetennis.style.backgroundColor = 'transparent';
  // stagecpam.style.backgroundColor = 'transparent';

  stageeffseit.style.color = '#313338';
  stageiyoo.style.color = '#dedede';
  // stagetennis.style.color = '#dedede';
  // stagecpam.style.color = '#dedede';
});


stageiyoo.addEventListener('click', function () {
  stageeffseittexte.style.display = 'none';
  stageeffseitBtn.style.display = 'none';
  stageiyootexte.style.display = 'block';
  stageiyooBtn.style.display = 'block';
  
  // stagetennistexte.style.color = 'transparent';
  // stagecpamtexte.style.color = 'transparent';

  stageeffseit.style.backgroundColor = 'transparent';
  stageiyoo.style.backgroundColor = '#dedede';
  // stagetennis.style.backgroundColor = 'transparent';
  // stagecpam.style.backgroundColor = 'transparent';

  stageeffseit.style.color = '#dedede';
  stageiyoo.style.color = '#313338';
  // stagetennis.style.color = '#dedede';
  // stagecpam.style.color = '#dedede';
});


// stagetennis.addEventListener('click', function () {
//   stageeffseittexte.style.color = 'transparent';
//   stageiyootexte.style.color = 'transparent';
//   // stagetennistexte.style.color = '#ffffff';
//   // stagecpamtexte.style.color = 'transparent';

//   stageeffseit.style.backgroundColor = 'transparent';
//   stageiyoo.style.backgroundColor = 'transparent';
//   // stagetennis.style.backgroundColor = '#dedede';
//   // stagecpam.style.backgroundColor = 'transparent';

//   stageeffseit.style.color = '#dedede';
//   stageiyoo.style.color = '#dedede';
//   // stagetennis.style.color = '#313338';
//   // stagecpam.style.color = '#dedede';
// });


// stagecpam.addEventListener('click', function () {
//   stageeffseittexte.style.color = 'transparent';
//   stageiyootexte.style.color = 'transparent';
//   stagetennistexte.style.color = 'transparent';
//   stagecpamtexte.style.color = '#ffffff';

//   stageeffseit.style.backgroundColor = 'transparent';
//   stageiyoo.style.backgroundColor = 'transparent';
//   stagetennis.style.backgroundColor = 'transparent';
//   stagecpam.style.backgroundColor = '#dedede';

//   stageeffseit.style.color = '#dedede';
//   stageiyoo.style.color = '#dedede';
//   stagetennis.style.color = '#dedede';
//   stagecpam.style.color = '#313338';
// });