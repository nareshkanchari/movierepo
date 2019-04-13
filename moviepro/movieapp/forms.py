from django import forms

class Book_Movie(forms.Form):

    movie_name=forms.CharField(
        label='Movie Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Movie Name'
            }
        )
    )
    Theaters=(
        ('sandhya theater at Rtc X road','sandhya theater at Rtc X road'),
        ('Viswanath 70MM Theater Kukatpally','Viswanath 70MM Theater Kukatpally'),
        ('Asian Lakshmikala Cinepride: Moosapet','Asian Lakshmikala Cinepride: Moosapet'),
        ('Cinepolis: Manjeera Mall, Kukatpally','Cinepolis: Manjeera Mall, Kukatpally'),
        ('PVR Forum Sujana Mall: Kukatpally, Hyderabad','PVR Forum Sujana Mall: Kukatpally, Hyderabad'),
        ('Cine Town: Miyapur','Cine Town: Miyapur'),
        ('PVR: Next Galleria Mall, Panjagutta','PVR: Next Galleria Mall, Panjagutta'),
        ('PVR: Inorbit, Cyberabad','PVR: Inorbit, Cyberabad'),
        ('Prasads: Hyderabad','Prasads: Hyderabad'),
        ('PVR Forum Sujana Mall: Kukatpally, Hyderabad','PVR Forum Sujana Mall: Kukatpally, Hyderabad')
    )

    theater_name=forms.ChoiceField(
        label='Select Theater',
        widget=forms.Select(
            attrs={
                'class':'form-control'
            }
        ),choices=Theaters)

    Shows=(
        ('morning','11:30'),
        ('matni','2:30'),
        ('evening','6:30'),
        ('night','9:30')
    )

    show_time=forms.ChoiceField(
        label='Select Show Time ',
        widget=forms.Select(
            attrs={
                'class':'form-control'
            }
        ),
        choices=Shows
    )

    Seats=(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10')
    )

    select_seats=forms.ChoiceField(
        label='Select Seats',
        widget=forms.Select(
            attrs={
                'class':'form-control'
            }
        ),
        choices=Seats
    )


