(()=>{'use strict';
 const btn=document.querySelector('.menu-toggle'), nav=document.querySelector('.site-nav');
 if(btn && nav){const close=()=>{nav.classList.remove('open');btn.setAttribute('aria-expanded','false');document.body.classList.remove('menu-open')};btn.addEventListener('click',()=>{const willOpen=!nav.classList.contains('open');nav.classList.toggle('open',willOpen);btn.setAttribute('aria-expanded',String(willOpen));document.body.classList.toggle('menu-open',willOpen)});nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',close));document.addEventListener('keydown',e=>{if(e.key==='Escape')close()})}
 const config=window.NOVIN_SITE_CONFIG||{};
 for(const [attr,val] of [['github',config.githubUrl],['email',config.email],['linkedin',config.linkedinUrl],['resume',config.resumeUrl],['figma',config.figmaPublicUrl]]){
  document.querySelectorAll(`[data-external="${attr}"]`).forEach(el=>{if(!val){el.hidden=true;return}el.hidden=false;el.href=attr==='email'?`mailto:${val}`:val;if(attr!=='email'){el.target='_blank';el.rel='noopener noreferrer'}});
 }
 document.querySelectorAll('[data-figma-status]').forEach(el=>{el.textContent=config.figmaPublicUrl?'Public Figma design link is available.':'Figma-ready editable files are included. Public Figma URL awaits publication.'});
 const tabs=[...document.querySelectorAll('[data-design-tab]')];const boards=[...document.querySelectorAll('.board[data-fidelity]')];
 if(tabs.length){const update=selected=>{tabs.forEach(tab=>{let on=tab.dataset.designTab===selected;tab.classList.toggle('active',on);tab.setAttribute('aria-pressed',String(on))});boards.forEach(board=>board.classList.toggle('show',board.dataset.fidelity===selected))};tabs.forEach(t=>t.addEventListener('click',()=>update(t.dataset.designTab)));update('low')}
 document.querySelectorAll('[data-year]').forEach(el=>el.textContent=new Date().getFullYear());
})();
