<html>
    <head>
        <title>Form</title>
        <style>



</style>
    </head>
    <body>
        <?php
        include("temp.php")
        ?>
        <div class="content" id="id02" >
           <div class="cont-img" >
           
              <h1>JOIN THE <br>
                  LEAGUE!

                </h1>
               
              
                     <div class="box1"></div>
                    <div class="box2"></div>
                    <div class="box3"></div>
                    <div class="box4"></div>
             </div>
        
  
            <div class="hometxt">
                     <div class="zz">
                     <button class="button1" onclick="document.getElementById('id01').style.display='block'">LOGIN</button> 
           
                         </div>
           
                <div id="id01" class="form">
                   <center> <h1>LOGIN</h1></center>
                   <br>
                   <br>
                   <form action="" method="post">
                       <label for="name">Username</label><br>
                       <input type="text" name="uname" placeholder="Enter Username">
                       <br>
                       <br>
                       <label for="password"> Password</label><br>
                       <input type="password"name="password"placeholder="Enter Password">
                      <br>
                      <br>
                      <br>
                      <br>
                       <button type="submit">LOGIN</button>
                       <br>
                       <br>
                       <button>  <a href="registration.php">  REGISTRATION</a></button>
                       <br>
                       <br>
                       <input type="checkbox" checked="checked"><b>REMEBER ME</b>
                   </form>
                </div>
                
            </div>
            
        </div>
        <div class="footer">
    <div class="box1"></div>
                            <div class="box2"></div>
                             <div class="box3"></div>
                             <div class="box4"></div>
    
    </div>
       
    </body>
</html>