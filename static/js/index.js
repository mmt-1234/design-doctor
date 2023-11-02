const imginput=document.querySelector('#file-input');
const imgbutt=document.querySelector('.upload-file');
const imagepre=document.querySelector('#img-preview');
const uploadFile=[];
const FileURl=[];

function createElement(e,file,num){
    const div=document.createElement('div');
    const img=document.createElement('img');

    div.setAttribute('class','element');
    div.setAttribute('onclick',format("Upload_File({0})",num));
    FileURl.push(e.target.result);
    img.setAttribute('src',e.target.result);
    img.setAttribute('data-file',file.name);
    img.setAttribute('class','img');
    img.setAttribute('style','width:50%; margin-left:25%');
    div.appendChild(img);

    return div;
}

function format() {
    var args = Array.prototype.slice.call (arguments, 1);
    return arguments[0].replace (/\{(\d+)\}/g, function (match, index) {
       return args[index];
    });
 }

function Upload_File(imgAddress){
    document.getElementById('main').src=FileURl[imgAddress];
}

function getImageInput(e){
    const files=e.currentTarget.files;
    if([...files].length>10){
        alert('이미지는 10개까지만 입력가능합니다');
        return;
    }
    var num=0;
    [...files].forEach(file => {
        if(!file.type.match("image/.*")){
            alert('이미지 파일만 업로드가 가능합니다');
            return;
        }
    
        uploadFile.push(file);
        const reader=new FileReader();
        reader.onload=(e)=>{
            const preview = createElement(e,file,FileURl.length);
            imagepre.appendChild(preview);
        };
        reader.readAsDataURL(file);
    });
}
imgbutt.addEventListener('click',()=>{
    imginput.click();
});
imginput.addEventListener('change',getImageInput);