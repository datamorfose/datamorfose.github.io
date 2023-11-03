import Filterizr from 'filterizr'
import { insertScript } from '../core'

document.addEventListener('DOMContentLoaded', () => {
  // ================== courses cards =====================

  // setup courses filter buttons
  const coursesCardHolder = document.getElementById('courses-card-holder')
  if (coursesCardHolder != null && coursesCardHolder.children.length !== 0) {
    // eslint-disable-next-line no-new
    new Filterizr('.filtr-courses', {
      layout: 'sameWidth',
      controlsSelector: '.courses-filtr-control'
    })
  }
})

// dynamically insert github buttons script.
insertScript('github-buttons', 'https://buttons.github.io/buttons.js')
