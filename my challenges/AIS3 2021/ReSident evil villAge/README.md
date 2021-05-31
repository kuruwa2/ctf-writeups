# ReSident evil villAge

## __Description__

<img src="https://user-images.githubusercontent.com/32315604/120188060-38b8c880-c248-11eb-9a5f-219cb5472156.png" width=300>

## __Solution__

Sign two messages whose product equals to the target message.

<img src="https://latex.codecogs.com/svg.image?\bg_black&space;m_1\times&space;m_2=m\Rightarrow&space;m_1^d\times&space;m_2^d=m^d\&space;(mod\&space;n)" title="\bg_black m_1\times m_2=m\Rightarrow m_1^d\times m_2^d=m^d\ (mod\ n)" />

For example, use <img src="https://latex.codecogs.com/gif.latex?\bg_black&space;163\times&space;33759323085949548325642458097" title="163\times 33759323085949548325642458097" /> as the [script](solve.py).

## __Unintended Solution__

Putting ```00``` before the target message can also bypass the rule.
