console.log("this is index.js");

//Book consrtuctor

function Book(bookname,author,booktype){
this.bookname=bookname;
this.author=author;
this.booktype=booktype;

}

//Display objeect
function Display(){

}
//clear functon

Display.prototype.clear=()=>{libraryform.reset();}

//Add function

Display.prototype.add=(book)=>{
    let tablebody=document.getElementById("tablebody");
    let uiString=` 
                <tr>
                
                <th scope="col">${book.bookname}</th>
                <th scope="col">${book.author}</th>
                <th scope="col">${book.booktype}</th>
            </tr> `;

    tablebody.innerHTML+=uiString;
}


//validation function
Display.prototype.validate=(book)=>
{
    if(book.bookname.length<3 || book.author.length<3)
    {
        return false;
    }

    else{
        return true;
    }

}

//Aleart function
Display.prototype.show=(type,dmessage)=>{
        let message=document.getElementById("message");
        message.innerHTML=`<div class="alert alert-${type} alert-dismissible fade show" role="alert" id="message">
        <strong>Holy guacamole!</strong> ${dmessage}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
      </div>`;
      setTimeout(()=>{message.innerHTML=""},2000);

}



//Add event Listener
let libraryform=document.getElementById("libraryform");
libraryform.addEventListener('submit',libraryformsubmit);
function libraryformsubmit(e){
    console.log("form submit");
    let bookname=document.getElementById("bookname").value;
    let author=document.getElementById("author").value;
    let booktype=""
    let fiction=document.getElementById("fiction");
    let programming=document.getElementById("programming");
    let cooking=document.getElementById("cooking");
    if(fiction.checked){booktype=fiction.value;}
    else if(programming.checked){booktype=programming.value;}
    else if(cooking.checked){booktype=cooking.value;}
    let book=new Book(bookname,author,booktype);
    console.log(book);
    let display=new Display();
    if(display.validate(book)){
        display.add(book);
        display.clear();
        display.show("success","rowadded");

    }
    else{
        display.show("danger","not added");
    }
    
    e.preventDefault();

}
