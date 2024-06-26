const username_field=document.querySelector('#username_field')
const feedback_field=document.querySelector('.invalid-username')

const email_field=document.querySelector('#emial_fieled')
username_field.addEventListener('keyup', (e)=> 
    {
        const username_value = e.target.value;

        if (username_value.length>0)
        {
            console.log(username_value); 
            fetch('/authentication/validate-username',
            {
                body:JSON.stringify({username: username_value}),
                method: "POST",
        
            })
            .then((res)=>res.json())
            .then((data)=>
            {
                console.log(data);
                if (data.username_error){
                    username_field.classList.add('is-invalid');
                    feedback_field.style.display = 'block';
                    feedback_field.innerHTML=`<p>${data.username_error}</p>`;
                } else {
                    username_field.classList.remove('is-invalid');
                    feedback_field.style.display = 'none';
                    feedback_field.innerHTML=``;
                }
            });
        };
    });