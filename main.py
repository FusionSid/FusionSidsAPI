"""
Our program, who art in memory,
    called by thy name;
  thy operating system run;
thy function be done at runtime
  as it was on development.
Give us this day our daily output.
And forgive us our code duplication,
    as we forgive those who
  duplicate code against us.
And lead us not into frustration;
  but deliver us from GOTOs.
    For thine is algorithm,
the computation, and the solution,
    looping forever and ever.
          Return;
"""

# If you are reading this code - I'm sorry

from fastapi import FastAPI

# Time for some imports which are all commented out lmao

# Image

# from routers.image.delete import delete
# from routers.image.rip import rip
# from routers.image.humansgood import humansgood
from routers.image.armor import armor
# from routers.image.plan import plan
from routers.image.brazzers import brazzers
# from routers.image.facts import facts
# from routers.image.batslap import batslap
# from routers.image.kimborder import kimborder
from routers.image.gun import gun
# from routers.image.garfield import garfield
# from routers.image.unpopular import unpopular
from routers.image.affect import affect
# from routers.image.hundred import hundred
# from routers.image.whothisis import whothisis
from routers.image.violence import violence
# from routers.image.screams import screams
# from routers.image.mom import mom
# from routers.image.corporate import corporate
# from routers.image.hitler import hitler
from routers.image.wanted import wanted
# from routers.image.spank import spank
# from routers.image.gay import gay
# from routers.image.ohno import ohno
# from routers.image.floor import floor
# from routers.image.emergencymeeting import emergencymeeting
# from routers.image.cheating import cheating
# from routers.image.boo import boo
# from routers.image.jail import jail
# from routers.image.satan import satan
# from routers.image.humanity import humanity
from routers.image.trash import trash
# from routers.image.brain import brain
# from routers.image.disability import disability
# from routers.image.presentation import presentation
from routers.image.aborted import aborted
# from routers.image.ugly import ugly
# from routers.image.fuck import fuck
# from routers.image.master import master
# from routers.image.failure import failure
# from routers.image.excuseme import excuseme
from routers.image.bongocat import bongocat
# from routers.image.piccolo import piccolo
# from routers.image.farmer import farmer
# from routers.image.door import door
# from routers.image.ban import ban
# from routers.image.expandingwwe import expandingwwe
from routers.image.surprised import surprised
# from routers.image.vr import vr
# from routers.image.inator import inator
# from routers.image.cry import cry
# from routers.image.nothing import nothing
# from routers.image.laid import laid
# from routers.image.obama import obama
# from routers.image.reticle import reticle
# from routers.image.bed import bed
# from routers.image.justpretending import justpretending
# from routers.image.note import note
from routers.image.abandon import abandon
# from routers.image.no_entry import no_entry
# from routers.image.goggles import goggles
# from routers.image.changemymind import changemymind
# from routers.image.balloon import balloon
# from routers.image.cancer import cancer
# from routers.image.ipad import ipad
# from routers.image.fakenews import fakenews
# from routers.image.confusedcat import confusedcat

# Other
from routers.other._8ball import eightball
from routers.other.qrcode import qrcode
from routers.other.roast import roast
from routers.other.compliment import compliment
from routers.other.random_meme import meme

# Description for api docs
description = """
### Made by FusionSid

[My Github](https://github.com/FusionSid)

This api mostly generates memes but it can also do roasts, 8ball qrcodes and more

#### Source Code:
[https://github.com/FusionSid/FusionSidsAPI](https://github.com/FusionSid/FusionSidsAPI)

#### Contact:
Discord: FusionSid#3645

#### LICENCE:
"""

# Creates an instance of the FastAPI class
app = FastAPI(
    title = "FusionSidsAPI",
    description=description,
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },

)

# Including all the endpoints:

# Other
app.include_router(router=roast)
app.include_router(router=qrcode)
app.include_router(router=eightball)
app.include_router(router=meme)
app.include_router(router=compliment)

# Image

# app.include_router(router=delete)
# app.include_router(router=rip)
# app.include_router(router=humansgood)
app.include_router(router=armor)
# app.include_router(router=plan)
app.include_router(router=brazzers)
# app.include_router(router=facts)
# app.include_router(router=batslap)
# app.include_router(router=kimborder)
app.include_router(router=gun)
# app.include_router(router=garfield)
# app.include_router(router=unpopular)
app.include_router(router=affect)
# app.include_router(router=hundred)
# app.include_router(router=whothisis)
app.include_router(router=violence)
# app.include_router(router=screams)
# app.include_router(router=mom)
# app.include_router(router=corporate)
# app.include_router(router=hitler)
app.include_router(router=wanted)
# app.include_router(router=spank)
# app.include_router(router=gay)
# app.include_router(router=ohno)
# app.include_router(router=floor)
# app.include_router(router=emergencymeeting)
# app.include_router(router=cheating)
# app.include_router(router=boo)
# app.include_router(router=jail)
# app.include_router(router=satan)
# app.include_router(router=humanity)
app.include_router(router=trash)
# app.include_router(router=brain)
# app.include_router(router=disability)
# app.include_router(router=presentation)
app.include_router(router=aborted)
# app.include_router(router=ugly)
# app.include_router(router=fuck)
# app.include_router(router=master)
# app.include_router(router=failure)
# app.include_router(router=excuseme)
app.include_router(router=bongocat)
# app.include_router(router=piccolo)
# app.include_router(router=farmer)
# app.include_router(router=door)
# app.include_router(router=ban)
# app.include_router(router=expandingwwe)
app.include_router(router=surprised)
# app.include_router(router=vr)
# app.include_router(router=inator)
# app.include_router(router=cry)
# app.include_router(router=nothing)
# app.include_router(router=laid)
# app.include_router(router=obama)
# app.include_router(router=reticle)
# app.include_router(router=bed)
# app.include_router(router=justpretending)
# app.include_router(router=note)
app.include_router(router=abandon)
# app.include_router(router=no_entry)
# app.include_router(router=goggles)
# app.include_router(router=changemymind)
# app.include_router(router=balloon)
# app.include_router(router=cancer)
# app.include_router(router=ipad)
# app.include_router(router=fakenews)
# app.include_router(router=confusedcat)
