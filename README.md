# PortScanner

This is a simple Port scanner I made for GCI. It have very easy useage as you will see :)

# Setup
1. Install git
<code>sudo apt-get install git</code>
1. Install python3
<code>sudo apt-get install python3</code>
2. Clone Repository
<code>git clone https://github.com/pascaaaal/PortScanner.git</code>
3. Go to folder
<code>cd PortScanner</code>
# Start
The basic usage is
<code>python3 scanner.py --ip <your.ip> --port <your port></code>
If you want to get the ports from a file, you can just use <code>--portF /path/to/file</code> instead of <code>--port <port></code>.

If you want the raw output you can use the <code>--format <true|false</code>. When you use <code>true</code> you will see the cli version.
when you use <code>false</code> you just get the output <code>port,open|closed</code>, witch you can use for other programs.

# Example
Some examples of use:
<br />
<code>python3 scanner.py --ip www.google.com --port 80</code>
<br />
Output:
<br />
<pre><code>Starting Port Scanner
Checking ports for www.google.com
Port 80      is open
Check finished: 1 open Ports, 0 closed Ports</code></pre>
<a href="https://asciinema.org/a/RAuoDnf2GeimdhCN9mgcFeC2R">asciinema</a>
<br />
<code>python3 scanner.py --ip www.google.com --port 80,443,8080</code>
<br />
Output:
<br />
<pre><code>Starting Port Scanner
Checking ports for www.google.com
Port 80      is open
Port 443     is open
Port 8080    is closed
Check finished: 2 open Ports, 1 closed Ports</code></pre>
<a href="https://asciinema.org/a/gCrMEvYfbXjyWUnPPrtBUe0bG">asciinema</a>
<br />
<code>python3 scanner.py --ip www.google.com --portF ports/web.txt</code>
<br />
Output:
<br />
<pre><code>Starting Port Scanner
Checking ports for www.google.com
Port 80      is open
Port 443     is open
Port 8080    is closed
Check finished: 2 open Ports, 1 closed Ports</code></pre>
<a href="https://asciinema.org/a/1mXFmusb7hrfGMKJ1jekLi0EE">asciinema</a>
<br />
<code>python3 scanner.py --ip www.google.com --portF ports/web.txt --format false</code>
<br />
Output:
<br />
<pre><code>80,open
443,open
8080,closed</code></pre>
<a href="https://asciinema.org/a/JTlekC8OlKWNEpxjBHZweDQvs">asciinema</a>
