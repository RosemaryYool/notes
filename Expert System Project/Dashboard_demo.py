from microdot import Microdot, Response

app = Microdot()
Response.default_content_type = 'text/html'

def htmldoc():
    doc = f'''
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Dashboard CSS - Demo</title>
            <link rel="stylesheet" href="https://williamedwardhahn.github.io/AI_Science_Medicine/dashboard.css">
        </head>
        <body>
            <header>
                <h1>Begin your study!</h1>
            </header>
            <nav>
                <input type="checkbox" id="nav-menu-btn" />
                <label for="nav-menu-btn"></label>
                <ul>
                    <li><a href="#">My Profile</a></li>
                    <li><a href="#">My Projects</a></li>
                    <li><a href="#">Color Selections</a></li>
                    <li><a href="#">System Calibration</a></li>
                </ul>
            </nav>
            <main class="container-fluid">
              <div class="row">

                <div class="col-xs-12 col-sm-6 col-md-3">
                  <div class="panel">
                    <header>
                      <h2>Temperature</h2>
                    </header>
                    <main>
                      <h3>23.5<sub>&deg;C</sub></h3>
                    </main>
                    <footer>
                      <time>2016_04_01 12:21 UTC</time>
                    </footer>
                  </div>
                </div>

                <div class="col-xs-12 col-sm-6 col-md-3">
                  <div class="panel">
                    <header>
                      <h2>M1 Position</h2>
                    </header>
                    <main>
                      <h3>14<sub>steps</sub></h3>
                    </main>
                    <footer>
                      <time>2016-04-01 12:21 UTC</time>
                    </footer>
                </div>
            </div>

        <div class="col-xs-12 col-sm-12 col-md-6">
          <div class="panel info">
            <header>
              <h2>Elapsed Time</h2>
            </header>
            <main>
              <h3>0:22:07.414</h3>
            </main>
            <footer>
              <time>2016-04-01 12:21 UTC</time>
            </footer>
          </div>
        </div>

      </div>

      <div class="row">

        <div class="col-xs-12 col-sm-12 col-md-6">
          <div class="panel double success">
            <header>
              <h2>Velocity Curves</h2>
            </header>
            <main>
              <img class="responsive" src="chart.svg" alt="Chart" />
            </main>
            <footer>
              <time>2016-04-01 12:21 UTC</time>
            </footer>
          </div>
        </div>

        <div class="col-xs-12 col-sm-12 col-md-6">
          <div class="panel double">
            <header>
              <h2>Motor Control</h2>
            </header>
            <main>
              <form>
                <div class="row">
                  <div class="col-md-3">
                    <label>Motor TL</label>
                    <input type="number" value="210" />
                  </div>
                  <div class="col-md-3">
                    <label>Motor TR</label>
                    <input type="number" value="0" />
                  </div>
                  <div class="col-md-3">
                    <label>Motor BL</label>
                    <input type="number" value="405" />
                  </div>
                  <div class="col-md-3">
                    <label>Motor BR</label>
                    <input type="number" value="313" />
                  </div>
                </div>
                <div class="row">
                  <div class="col-md-3">
                    <label>Trim TL</label>
                    <input type="number" value="14" />
                  </div>
                  <div class="col-md-3">
                    <label>Trim TR</label>
                    <input type="number" value="0" />
                  </div>
                  <div class="col-md-3">
                    <label>Trim BL</label>
                    <input type="number" value="0" />
                  </div>
                  <div class="col-md-3">
                    <label>Trim BR</label>
                    <input type="number" value="-10" />
                  </div>
                </div>

                <button class="info">Apply</button>
                <button class="warning">Execute</button>
                <button class="danger">Halt</button>
              </form>
            </main>
          </div>
        </div>

      </div>

    </main>
    <footer>
      <p>
        <small>
        MPCR Lab
        </small>
      </p>
    </footer>
  </body>
</html>
'''
    return doc


@app.route('/')
def serve_html(request):
    return htmldoc()

app.run(debug=True, port=8011)
