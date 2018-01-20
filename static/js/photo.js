function photo(){
    const request = new XMLHttpRequest();
    request.open("GET","http://127.0.0.1:5000/photo");
    request.addEventListener("load",(event) =>{
        if(event.target.status !== 200){
            console.log('Error: ${event.target.status}');
            return;
        }
        console.log(event.target.status);
        console.log(event.target.responseText);
    })
    request.addEventListener("error",() =>{
        console.log('Network Error');
    })
    request.send();
}