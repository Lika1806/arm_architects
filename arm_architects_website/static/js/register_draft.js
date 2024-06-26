const username_field=document.querySelector('#username_field')
const invalid_username_feedback=document.querySelector('.invalid-username')

const email_field=document.querySelector('#email_fieled')
const invalid_email_feedback=document.querySelector('.invalid-email')

email_field.addEventListener('keyup', (e)=>
{
    const email_value = e.target.value;
    if (email_value.length>0)
    {
        console.log(email_value);
        fetch('/authentication/validate-email',
        {
            body: JSON.stringify({email: email_value}),
            method: "POST",
        })
        .then((res)=>res.json())
        .then((data)=>
        {
            console.log(data);
            if (data.email_error){
                email_field.classList.add('is-invalid');
                invalid_email_feedback.style.display = 'block';
                invalid_email_feedback.innerHTML=`<p>${data.username_error}</p>`;
            } else {
                email_field.classList.remove('is-invalid');
                invalid_email_feedback.style.display = 'none';
                invalid_email_feedback.innerHTML=``;
            }
    });
};
});
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
                    invalid_username_feedback.style.display = 'block';
                    invalid_username_feedback.innerHTML=`<p>${data.username_error}</p>`;
                } else {
                    username_field.classList.remove('is-invalid');
                    invalid_username_feedback.style.display = 'none';
                    invalid_username_feedback.innerHTML=``;
                }
            });
        };
    });