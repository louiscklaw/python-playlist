import React from 'react'

function ResultCard(props){
  return(
    <>
      <div class="card">
        <header class="card-header">
          <h3 class="card-header-title">TestStringMethods1</h3>
        </header>

        <div class="result-tile">
          <div class="result-grid-wrapper">

            <div class="box1">P</div>
            <div class="box2">E</div>
            <div class="box3">S</div>
            <div class="box4">F</div>


            <div class="box1">1</div>
            <div class="box2"></div>
            <div class="box3"></div>
            <div class="box4"></div>

            <div class="box1">1</div>
            <div class="box2"></div>
            <div class="box3"></div>
            <div class="box4"></div>

            <div class="box1">1</div>
            <div class="box2"></div>
            <div class="box3"></div>
            <div class="box4"></div>

            <div class="box1">1</div>
            <div class="box2"></div>
            <div class="box3"></div>
            <div class="box4"></div>
          </div>

        </div>
        <div class="card-content">
          <div class="media">
            <div class="media-content">

            </div>
          </div>

          <div class="content">
            testing the outlook of the page
            <br><a>@bulmaio</a>.
            <br><a href="#">#css</a>
            <br><a href="#">#responsive</a>
            <br>
            <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
          </div>
        </div>
      </div>
    </>
  )
}

export default ResultCard