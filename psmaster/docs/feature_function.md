# Feature function

## **x**(*s*): vector of features visible when in state *s*
The binary representation is constructed by first assigning indices, from 0 to *n - 1*, to all states. Then, the binary encoding of the state index is used as a feature vector to represent that state. The length of a feature vector is determined by the total number of states.

**My active pokemon (Main)**

| State | Description | Active | Inactive |
| :---: | :--- | :---: | :---: |
| *s<sub>0* | fnt | 1 | 0 |
| *s<sub>1* | p1 | 1 | 0 |
| *s<sub>2* | p2 | 1 | 0 |
| *s<sub>3* | p3 | 1 | 0 |
| *s<sub>4* | p4 | 1 | 0 |
| *s<sub>5* | p5 | 1 | 0 |
| *s<sub>6* | p6 | 1 | 0 |
| *s<sub>7* | HP >= 90% | 1 | 0 |
| *s<sub>8* | 70% <= HP < 90% | 1 | 0 |
| *s<sub>9* | 50% <= HP < 70% | 1 | 0 |
| *s<sub>10* | 30% <= HP < 50% | 1 | 0 |
| *s<sub>11* | 10% <= HP < 30% | 1 | 0 |
| *s<sub>12* | HP < 10% | 1 | 0 |
| *s<sub>13* | brn | 1 | 0 |
| *s<sub>14* | frz | 1 | 0 |
| *s<sub>15* | par | 1 | 0 |
| *s<sub>16* | psn | 1 | 0 |
| *s<sub>17* | slp | 1 | 0 |
| *s<sub>18* | boost Atk | 1 | 0 |
| *s<sub>19* | boost Atk (>= +3) | 1 | 0 |
| *s<sub>20* | unboost Atk | 1 | 0 |
| *s<sub>21* | boost Def | 1 | 0 |
| *s<sub>22* | boost Def (>= +3) | 1 | 0 |
| *s<sub>23* | unboost Def | 1 | 0 |
| *s<sub>24* | boost SpA | 1 | 0 |
| *s<sub>25* | boost SpA (>= +3) | 1 | 0 |
| *s<sub>26* | unboost SpA | 1 | 0 |
| *s<sub>27* | boost SpD | 1 | 0 |
| *s<sub>28* | boost SpD (>= +3) | 1 | 0 |
| *s<sub>29* | unboost SpD | 1 | 0 |
| *s<sub>30* | boost Spe | 1 | 0 |
| *s<sub>31* | boost Spe (>= +3) | 1 | 0 |
| *s<sub>32* | unboost Spe | 1 | 0 |
| *s<sub>33* | boost accuracy | 1 | 0 |
| *s<sub>34* | unboost accuracy | 1 | 0 |
| *s<sub>35* | boost evasion | 1 | 0 |
| *s<sub>36* | unboost evasion | 1 | 0 |
| *s<sub>37* | p1 switchable | 1 | 0 |
| *s<sub>38* | p2 switchable | 1 | 0 |
| *s<sub>39* | p3 switchable | 1 | 0 |
| *s<sub>40* | p4 switchable | 1 | 0 |
| *s<sub>41* | p5 switchable | 1 | 0 |
| *s<sub>42* | p6 switchable | 1 | 0 |
| *s<sub>43* | Spikes | 1 | 0 |
| *s<sub>44* | Stealth Rock | 1 | 0 |
| *s<sub>45* | Sticky Web | 1 | 0 |
| *s<sub>46* | Toxic Spikes | 1 | 0 |
| *s<sub>47* | Reflect | 1 | 0 |
| *s<sub>48* | Light Screen | 1 | 0 |
| *s<sub>49* | Aurora Veil | 1 | 0 |
| *s<sub>50* | Tailwind | 1 | 0 |

**Opponent's active pokemon (Main)**

| State | Description | Active | Inactive |
| :---: | :--- | :---: | :---: |
| *s<sub>51* | fnt | 1 | 0 |
| *s<sub>52* | Bug | 1 | 0 |
| *s<sub>53* | Dark | 1 | 0 |
| *s<sub>54* | Dragon | 1 | 0 |
| *s<sub>55* | Electric | 1 | 0 |
| *s<sub>56* | Fairy | 1 | 0 |
| *s<sub>57* | Fighting | 1 | 0 |
| *s<sub>58* | Fire | 1 | 0 |
| *s<sub>59* | Flying | 1 | 0 |
| *s<sub>60* | Ghost | 1 | 0 |
| *s<sub>61* | Grass | 1 | 0 |
| *s<sub>62* | Ground | 1 | 0 |
| *s<sub>63* | Ice | 1 | 0 |
| *s<sub>64* | Normal | 1 | 0 |
| *s<sub>65* | Poison | 1 | 0 |
| *s<sub>66* | Psychic | 1 | 0 |
| *s<sub>67* | Rock | 1 | 0 |
| *s<sub>68* | Steel | 1 | 0 |
| *s<sub>69* | Water | 1 | 0 |
| *s<sub>70* | highest: HP | 1 | 0 |
| *s<sub>71* | highest: Atk | 1 | 0 |
| *s<sub>72* | highest: Def | 1 | 0 |
| *s<sub>73* | highest: SpA | 1 | 0 |
| *s<sub>74* | highest: SpD | 1 | 0 |
| *s<sub>75* | highest: Spe | 1 | 0 |
| *s<sub>76* | 2nd highest: HP | 1 | 0 |
| *s<sub>77* | 2nd highest: Atk | 1 | 0 |
| *s<sub>78* | 2nd highest: Def | 1 | 0 |
| *s<sub>79* | 2nd highest: SpA | 1 | 0 |
| *s<sub>80* | 2nd highest: SpD | 1 | 0 |
| *s<sub>81* | 2nd highest: Spe | 1 | 0 |
| *s<sub>82* | lowest: HP | 1 | 0 |
| *s<sub>83* | lowest: Atk | 1 | 0 |
| *s<sub>84* | lowest: Def | 1 | 0 |
| *s<sub>85* | lowest: SpA | 1 | 0 |
| *s<sub>86* | lowest: SpD | 1 | 0 |
| *s<sub>87* | lowest: Spe | 1 | 0 |
| *s<sub>88* | 2nd lowest: HP | 1 | 0 |
| *s<sub>89* | 2nd lowest: Atk | 1 | 0 |
| *s<sub>90* | 2nd lowest: Def | 1 | 0 |
| *s<sub>91* | 2nd lowest: SpA | 1 | 0 |
| *s<sub>92* | 2nd lowest: SpD | 1 | 0 |
| *s<sub>93* | 2nd lowest: Spe | 1 | 0 |
| *s<sub>94* | HP >= 90% | 1 | 0 |
| *s<sub>95* | 70% <= HP < 90% | 1 | 0 |
| *s<sub>96* | 50% <= HP < 70% | 1 | 0 |
| *s<sub>97* | 30% <= HP < 50% | 1 | 0 |
| *s<sub>98* | 10% <= HP < 30% | 1 | 0 |
| *s<sub>99* | HP < 10% | 1 | 0 |
| *s<sub>100* | brn | 1 | 0 |
| *s<sub>101* | frz | 1 | 0 |
| *s<sub>102* | par | 1 | 0 |
| *s<sub>103* | psn | 1 | 0 |
| *s<sub>104* | slp | 1 | 0 |
| *s<sub>105* | boost Atk | 1 | 0 |
| *s<sub>106* | boost Atk (>= +3) | 1 | 0 |
| *s<sub>107* | unboost Atk | 1 | 0 |
| *s<sub>108* | boost Def | 1 | 0 |
| *s<sub>109* | boost Def (>= +3) | 1 | 0 |
| *s<sub>110* | unboost Def | 1 | 0 |
| *s<sub>111* | boost SpA | 1 | 0 |
| *s<sub>112* | boost SpA (>= +3) | 1 | 0 |
| *s<sub>113* | unboost SpA | 1 | 0 |
| *s<sub>114* | boost SpD | 1 | 0 |
| *s<sub>115* | boost SpD (>= +3) | 1 | 0 |
| *s<sub>116* | unboost SpD | 1 | 0 |
| *s<sub>117* | boost Spe | 1 | 0 |
| *s<sub>118* | boost Spe (>= +3) | 1 | 0 |
| *s<sub>119* | unboost Spe | 1 | 0 |
| *s<sub>120* | boost accuracy | 1 | 0 |
| *s<sub>121* | unboost accuracy | 1 | 0 |
| *s<sub>122* | boost evasion | 1 | 0 |
| *s<sub>123* | unboost evasion | 1 | 0 |
| *s<sub>124* | Bug switchable | 1 | 0 |
| *s<sub>125* | Dark switchable | 1 | 0 |
| *s<sub>126* | Dragon switchable | 1 | 0 |
| *s<sub>127* | Electric switchable | 1 | 0 |
| *s<sub>128* | Fairy switchable | 1 | 0 |
| *s<sub>129* | Fighting switchable | 1 | 0 |
| *s<sub>130* | Fire switchable | 1 | 0 |
| *s<sub>131* | Flying switchable | 1 | 0 |
| *s<sub>132* | Ghost switchable | 1 | 0 |
| *s<sub>133* | Grass switchable | 1 | 0 |
| *s<sub>134* | Ground switchable | 1 | 0 |
| *s<sub>135* | Ice switchable | 1 | 0 |
| *s<sub>136* | Normal switchable | 1 | 0 |
| *s<sub>137* | Poison switchable | 1 | 0 |
| *s<sub>138* | Psychic switchable | 1 | 0 |
| *s<sub>139* | Rock switchable | 1 | 0 |
| *s<sub>140* | Steel switchable | 1 | 0 |
| *s<sub>141* | Water switchable | 1 | 0 |
| *s<sub>142* | Spikes | 1 | 0 |
| *s<sub>143* | Stealth Rock | 1 | 0 |
| *s<sub>144* | Sticky Web | 1 | 0 |
| *s<sub>145* | Toxic Spikes | 1 | 0 |
| *s<sub>146* | Reflect | 1 | 0 |
| *s<sub>147* | Light Screen | 1 | 0 |
| *s<sub>148* | Aurora Veil | 1 | 0 |
| *s<sub>149* | Tailwind | 1 | 0 |

**Both sides**

| State | Description | Active | Inactive |
| :---: | :--- | :---: | :---: |
| *s<sub>150* | Harsh sunlight | 1 | 0 |
| *s<sub>151* | Rain | 1 | 0 |
| *s<sub>152* | Sandstorm | 1 | 0 |
| *s<sub>153* | Hail | 1 | 0 |
| *s<sub>154* | Extremely harsh sunlight | 1 | 0 |
| *s<sub>155* | Heavy rain | 1 | 0 |
| *s<sub>156* | Electric Terrain | 1 | 0 |
| *s<sub>157* | Grassy Terrain | 1 | 0 |
| *s<sub>158* | Misty Terrain | 1 | 0 |
| *s<sub>159* | Psychic Terrain | 1 | 0 |

**My active pokemon (Status)**

| State | Description | Active | Inactive |
| :---: | :--- | :---: | :---: |
| *s<sub>160* | Bound | 1 | 0 |
| *s<sub>161* | Can't escape | 1 | 0 |
| *s<sub>162* | Confusion | 1 | 0 |
| *s<sub>163* | Curse | 1 | 0 |
| *s<sub>164* | Embargo | 1 | 0 |
| *s<sub>165* | Encore | 1 | 0 |
| *s<sub>166* | Heal Block | 1 | 0 |
| *s<sub>167* | Identified | 1 | 0 |
| *s<sub>168* | Infatuation | 1 | 0 |
| *s<sub>169* | Leech Seed | 1 | 0 |
| *s<sub>170* | Nightmare | 1 | 0 |
| *s<sub>171* | Perish Song | 1 | 0 |
| *s<sub>172* | Taunt | 1 | 0 |
| *s<sub>173* | Telekinesis | 1 | 0 |
| *s<sub>174* | Torment | 1 | 0 |
| *s<sub>175* | Aqua Ring | 1 | 0 |
| *s<sub>176* | Charging turn | 1 | 0 |
| *s<sub>177* | Defense Curl | 1 | 0 |
| *s<sub>178* | Rooting | 1 | 0 |
| *s<sub>179* | Magnetic levitation | 1 | 0 |
| *s<sub>180* | Recharging | 1 | 0 |
| *s<sub>181* | Semi-invulnerable | 1 | 0 |
| *s<sub>182* | Substitute | 1 | 0 |
| *s<sub>183* | Taking aim | 1 | 0 |
| *s<sub>184* | Withdrawing | 1 | 0 |

**Opponent's active pokemon (Status)**

| State | Description | Active | Inactive |
| :---: | :--- | :---: | :---: |
| *s<sub>185* | Bound | 1 | 0 |
| *s<sub>186* | Can't escape | 1 | 0 |
| *s<sub>187* | Confusion | 1 | 0 |
| *s<sub>188* | Curse | 1 | 0 |
| *s<sub>189* | Embargo | 1 | 0 |
| *s<sub>190* | Encore | 1 | 0 |
| *s<sub>191* | Heal Block | 1 | 0 |
| *s<sub>192* | Identified | 1 | 0 |
| *s<sub>193* | Infatuation | 1 | 0 |
| *s<sub>194* | Leech Seed | 1 | 0 |
| *s<sub>195* | Nightmare | 1 | 0 |
| *s<sub>196* | Perish Song | 1 | 0 |
| *s<sub>197* | Taunt | 1 | 0 |
| *s<sub>198* | Telekinesis | 1 | 0 |
| *s<sub>199* | Torment | 1 | 0 |
| *s<sub>200* | Aqua Ring | 1 | 0 |
| *s<sub>201* | Charging turn | 1 | 0 |
| *s<sub>202* | Defense Curl | 1 | 0 |
| *s<sub>203* | Rooting | 1 | 0 |
| *s<sub>204* | Magnetic levitation | 1 | 0 |
| *s<sub>205* | Recharging | 1 | 0 |
| *s<sub>206* | Semi-invulnerable | 1 | 0 |
| *s<sub>207* | Substitute | 1 | 0 |
| *s<sub>208* | Taking aim | 1 | 0 |
| *s<sub>209* | Withdrawing | 1 | 0 |

**Backups**

| State | Description | Active | Inactive |
| :---: | :--- | :---: | :---: |
| *s<sub>210* | backup1 | 1 | 0 |
| *s<sub>211* | backup2 | 1 | 0 |
| *s<sub>212* | backup3 | 1 | 0 |
| *s<sub>213* | backup4 | 1 | 0 |
| *s<sub>214* | backup5 | 1 | 0 |
| *s<sub>215* | backup6 | 1 | 0 |
| *s<sub>216* | backup7 | 1 | 0 |
| *s<sub>217* | backup8 | 1 | 0 |
| *s<sub>218* | backup9 | 1 | 0 |
| *s<sub>219* | backup10 | 1 | 0 |
| *s<sub>220* | backup11 | 1 | 0 |
| *s<sub>221* | backup12 | 1 | 0 |
| *s<sub>222* | backup13 | 1 | 0 |
| *s<sub>223* | backup14 | 1 | 0 |
| *s<sub>224* | backup15 | 1 | 0 |

Therefore, *n* = |**x**(*s*)| = 225

## **x**(*s*, *a*): vector of features visible when in state *s* taking action *a*
A common way to derive an action-feature vector **x**(*s*, *a*) from a state-feature vector **x**(*s*) involves an action-feature vector of size *n*|*A*|, where *n* is the number of state features and |*A*| is the number of actions. Each action corresponds with a block of *n* features in this action-feature vector. The features in **x**(*s*, *a*) that corresponds to action *a* take on the values of the state features; the features corresponding to other actions have a value of 0.
