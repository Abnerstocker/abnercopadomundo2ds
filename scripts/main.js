document.addEventListener('DOMContentLoaded', function(){
  // Accordion
  document.querySelectorAll('[data-accordion] .accordion-item').forEach(btn => {
    btn.addEventListener('click', function(){
      const panel = this.nextElementSibling;
      const open = panel.style.display === 'block';
      // close all
      document.querySelectorAll('[data-accordion] .accordion-panel').forEach(p => p.style.display = 'none');
      if(!open){
        panel.style.display = 'block';
      }
    });
  });

  // Hamburger toggle (simple)
  const hamb = document.querySelector('.hamburger');
  if(hamb){
    hamb.addEventListener('click', ()=>{
      const center = document.querySelector('.nav-center');
      if(center.style.display === 'flex'){
        center.style.display = 'none';
      } else {
        center.style.display = 'flex';
        center.style.flexDirection = 'column';
      }
    });
  }
});
