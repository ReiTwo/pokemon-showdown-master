# Feature function
There are mainly three representations of the feature function: *tabular*, *binary* and *non-binary*. For Pokemon Showdown, tabular features are infeasible due to an overly large state-action space, so I decided to go with the simple binary representation. On the other hand, I believe that the non-binary representation will achieve a better result, but it is more complicated (lazy . . .) to implement as compared to the binary representation.

## **x**(*s*): vector of features visible when in state *s*
The binary representation is constructed by first assigning indices, from 0 to *n - 1*, to all states. Then, the binary encoding of the state index is used as a feature vector to represent that state. The length of a feature vector is determined by the total number of states.

**My active pokemon (Main)**

| State | Description | Active | Inactive |
| :---: | :--- | :---: | :---: |
| *s<sub>0</sub>* | fnt | 1 | 0 |
| *s<sub>1</sub>* | p1 | 1 | 0 |
| *s<sub>2</sub>* | p2 | 1 | 0 |
| *s<sub>3</sub>* | p3 | 1 | 0 |
| *s<sub>4</sub>* | p4 | 1 | 0 |
| *s<sub>5</sub>* | p5 | 1 | 0 |
| *s<sub>6</sub>* | p6 | 1 | 0 |
| *s<sub>7</sub>* | HP >= 90% | 1 | 0 |
| *s<sub>8</sub>* | 70% <= HP < 90% | 1 | 0 |
| *s<sub>9</sub>* | 50% <= HP < 70% | 1 | 0 |
| *s<sub>10</sub>* | 30% <= HP < 50% | 1 | 0 |
| *s<sub>11</sub>* | 10% <= HP < 30% | 1 | 0 |
| *s<sub>12</sub>* | HP < 10% | 1 | 0 |
| *s<sub>13</sub>* | brn | 1 | 0 |
| *s<sub>14</sub>* | frz | 1 | 0 |
| *s<sub>15</sub>* | par | 1 | 0 |
| *s<sub>16</sub>* | psn | 1 | 0 |
| *s<sub>17</sub>* | slp | 1 | 0 |
| *s<sub>18</sub>* | boost Atk | 1 | 0 |
| *s<sub>19</sub>* | boost Atk (>= +3) | 1 | 0 |
| *s<sub>20</sub>* | unboost Atk | 1 | 0 |
| *s<sub>21</sub>* | boost Def | 1 | 0 |
| *s<sub>22</sub>* | boost Def (>= +3) | 1 | 0 |
| *s<sub>23</sub>* | unboost Def | 1 | 0 |
| *s<sub>24</sub>* | boost SpA | 1 | 0 |
| *s<sub>25</sub>* | boost SpA (>= +3) | 1 | 0 |
| *s<sub>26</sub>* | unboost SpA | 1 | 0 |
| *s<sub>27</sub>* | boost SpD | 1 | 0 |
| *s<sub>28</sub>* | boost SpD (>= +3) | 1 | 0 |
| *s<sub>29</sub>* | unboost SpD | 1 | 0 |
| *s<sub>30</sub>* | boost Spe | 1 | 0 |
| *s<sub>31</sub>* | boost Spe (>= +3) | 1 | 0 |
| *s<sub>32</sub>* | unboost Spe | 1 | 0 |
| *s<sub>33</sub>* | boost accuracy | 1 | 0 |
| *s<sub>34</sub>* | unboost accuracy | 1 | 0 |
| *s<sub>35</sub>* | boost evasion | 1 | 0 |
| *s<sub>36</sub>* | unboost evasion | 1 | 0 |
| *s<sub>37</sub>* | p1 switchable | 1 | 0 |
| *s<sub>38</sub>* | p2 switchable | 1 | 0 |
| *s<sub>39</sub>* | p3 switchable | 1 | 0 |
| *s<sub>40</sub>* | p4 switchable | 1 | 0 |
| *s<sub>41</sub>* | p5 switchable | 1 | 0 |
| *s<sub>42</sub>* | p6 switchable | 1 | 0 |
| *s<sub>43</sub>* | Spikes | 1 | 0 |
| *s<sub>44</sub>* | Stealth Rock | 1 | 0 |
| *s<sub>45</sub>* | Sticky Web | 1 | 0 |
| *s<sub>46</sub>* | Toxic Spikes | 1 | 0 |
| *s<sub>47</sub>* | Reflect | 1 | 0 |
| *s<sub>48</sub>* | Light Screen | 1 | 0 |
| *s<sub>49</sub>* | Aurora Veil | 1 | 0 |
| *s<sub>50</sub>* | Tailwind | 1 | 0 |

**Opponent's active pokemon (Main)**

| State | Description | Active | Inactive |
| :---: | :--- | :---: | :---: |
| *s<sub>51</sub>* | fnt | 1 | 0 |
| *s<sub>52</sub>* | Bug | 1 | 0 |
| *s<sub>53</sub>* | Dark | 1 | 0 |
| *s<sub>54</sub>* | Dragon | 1 | 0 |
| *s<sub>55</sub>* | Electric | 1 | 0 |
| *s<sub>56</sub>* | Fairy | 1 | 0 |
| *s<sub>57</sub>* | Fighting | 1 | 0 |
| *s<sub>58</sub>* | Fire | 1 | 0 |
| *s<sub>59</sub>* | Flying | 1 | 0 |
| *s<sub>60</sub>* | Ghost | 1 | 0 |
| *s<sub>61</sub>* | Grass | 1 | 0 |
| *s<sub>62</sub>* | Ground | 1 | 0 |
| *s<sub>63</sub>* | Ice | 1 | 0 |
| *s<sub>64</sub>* | Normal | 1 | 0 |
| *s<sub>65</sub>* | Poison | 1 | 0 |
| *s<sub>66</sub>* | Psychic | 1 | 0 |
| *s<sub>67</sub>* | Rock | 1 | 0 |
| *s<sub>68</sub>* | Steel | 1 | 0 |
| *s<sub>69</sub>* | Water | 1 | 0 |
| *s<sub>70</sub>* | highest: HP | 1 | 0 |
| *s<sub>71</sub>* | highest: Atk | 1 | 0 |
| *s<sub>72</sub>* | highest: Def | 1 | 0 |
| *s<sub>73</sub>* | highest: SpA | 1 | 0 |
| *s<sub>74</sub>* | highest: SpD | 1 | 0 |
| *s<sub>75</sub>* | highest: Spe | 1 | 0 |
| *s<sub>76</sub>* | 2nd highest: HP | 1 | 0 |
| *s<sub>77</sub>* | 2nd highest: Atk | 1 | 0 |
| *s<sub>78</sub>* | 2nd highest: Def | 1 | 0 |
| *s<sub>79</sub>* | 2nd highest: SpA | 1 | 0 |
| *s<sub>80</sub>* | 2nd highest: SpD | 1 | 0 |
| *s<sub>81</sub>* | 2nd highest: Spe | 1 | 0 |
| *s<sub>82</sub>* | lowest: HP | 1 | 0 |
| *s<sub>83</sub>* | lowest: Atk | 1 | 0 |
| *s<sub>84</sub>* | lowest: Def | 1 | 0 |
| *s<sub>85</sub>* | lowest: SpA | 1 | 0 |
| *s<sub>86</sub>* | lowest: SpD | 1 | 0 |
| *s<sub>87</sub>* | lowest: Spe | 1 | 0 |
| *s<sub>88</sub>* | 2nd lowest: HP | 1 | 0 |
| *s<sub>89</sub>* | 2nd lowest: Atk | 1 | 0 |
| *s<sub>90</sub>* | 2nd lowest: Def | 1 | 0 |
| *s<sub>91</sub>* | 2nd lowest: SpA | 1 | 0 |
| *s<sub>92</sub>* | 2nd lowest: SpD | 1 | 0 |
| *s<sub>93</sub>* | 2nd lowest: Spe | 1 | 0 |
| *s<sub>94</sub>* | HP >= 90% | 1 | 0 |
| *s<sub>95</sub>* | 70% <= HP < 90% | 1 | 0 |
| *s<sub>96</sub>* | 50% <= HP < 70% | 1 | 0 |
| *s<sub>97</sub>* | 30% <= HP < 50% | 1 | 0 |
| *s<sub>98</sub>* | 10% <= HP < 30% | 1 | 0 |
| *s<sub>99</sub>* | HP < 10% | 1 | 0 |
| *s<sub>100</sub>* | brn | 1 | 0 |
| *s<sub>101</sub>* | frz | 1 | 0 |
| *s<sub>102</sub>* | par | 1 | 0 |
| *s<sub>103</sub>* | psn | 1 | 0 |
| *s<sub>104</sub>* | slp | 1 | 0 |
| *s<sub>105</sub>* | boost Atk | 1 | 0 |
| *s<sub>106</sub>* | boost Atk (>= +3) | 1 | 0 |
| *s<sub>107</sub>* | unboost Atk | 1 | 0 |
| *s<sub>108</sub>* | boost Def | 1 | 0 |
| *s<sub>109</sub>* | boost Def (>= +3) | 1 | 0 |
| *s<sub>110</sub>* | unboost Def | 1 | 0 |
| *s<sub>111</sub>* | boost SpA | 1 | 0 |
| *s<sub>112</sub>* | boost SpA (>= +3) | 1 | 0 |
| *s<sub>113</sub>* | unboost SpA | 1 | 0 |
| *s<sub>114</sub>* | boost SpD | 1 | 0 |
| *s<sub>115</sub>* | boost SpD (>= +3) | 1 | 0 |
| *s<sub>116</sub>* | unboost SpD | 1 | 0 |
| *s<sub>117</sub>* | boost Spe | 1 | 0 |
| *s<sub>118</sub>* | boost Spe (>= +3) | 1 | 0 |
| *s<sub>119</sub>* | unboost Spe | 1 | 0 |
| *s<sub>120</sub>* | boost accuracy | 1 | 0 |
| *s<sub>121</sub>* | unboost accuracy | 1 | 0 |
| *s<sub>122</sub>* | boost evasion | 1 | 0 |
| *s<sub>123</sub>* | unboost evasion | 1 | 0 |
| *s<sub>124</sub>* | Bug switchable | 1 | 0 |
| *s<sub>125</sub>* | Dark switchable | 1 | 0 |
| *s<sub>126</sub>* | Dragon switchable | 1 | 0 |
| *s<sub>127</sub>* | Electric switchable | 1 | 0 |
| *s<sub>128</sub>* | Fairy switchable | 1 | 0 |
| *s<sub>129</sub>* | Fighting switchable | 1 | 0 |
| *s<sub>130</sub>* | Fire switchable | 1 | 0 |
| *s<sub>131</sub>* | Flying switchable | 1 | 0 |
| *s<sub>132</sub>* | Ghost switchable | 1 | 0 |
| *s<sub>133</sub>* | Grass switchable | 1 | 0 |
| *s<sub>134</sub>* | Ground switchable | 1 | 0 |
| *s<sub>135</sub>* | Ice switchable | 1 | 0 |
| *s<sub>136</sub>* | Normal switchable | 1 | 0 |
| *s<sub>137</sub>* | Poison switchable | 1 | 0 |
| *s<sub>138</sub>* | Psychic switchable | 1 | 0 |
| *s<sub>139</sub>* | Rock switchable | 1 | 0 |
| *s<sub>140</sub>* | Steel switchable | 1 | 0 |
| *s<sub>141</sub>* | Water switchable | 1 | 0 |
| *s<sub>142</sub>* | Spikes | 1 | 0 |
| *s<sub>143</sub>* | Stealth Rock | 1 | 0 |
| *s<sub>144</sub>* | Sticky Web | 1 | 0 |
| *s<sub>145</sub>* | Toxic Spikes | 1 | 0 |
| *s<sub>146</sub>* | Reflect | 1 | 0 |
| *s<sub>147</sub>* | Light Screen | 1 | 0 |
| *s<sub>148</sub>* | Aurora Veil | 1 | 0 |
| *s<sub>149</sub>* | Tailwind | 1 | 0 |

**Both sides**

| State | Description | Active | Inactive |
| :---: | :--- | :---: | :---: |
| *s<sub>150</sub>* | Harsh sunlight | 1 | 0 |
| *s<sub>151</sub>* | Rain | 1 | 0 |
| *s<sub>152</sub>* | Sandstorm | 1 | 0 |
| *s<sub>153</sub>* | Hail | 1 | 0 |
| *s<sub>154</sub>* | Extremely harsh sunlight | 1 | 0 |
| *s<sub>155</sub>* | Heavy rain | 1 | 0 |
| *s<sub>156</sub>* | Electric Terrain | 1 | 0 |
| *s<sub>157</sub>* | Grassy Terrain | 1 | 0 |
| *s<sub>158</sub>* | Misty Terrain | 1 | 0 |
| *s<sub>159</sub>* | Psychic Terrain | 1 | 0 |

**My active pokemon (Status)**

| State | Description | Active | Inactive |
| :---: | :--- | :---: | :---: |
| *s<sub>160</sub>* | Bound | 1 | 0 |
| *s<sub>161</sub>* | Can't escape | 1 | 0 |
| *s<sub>162</sub>* | Confusion | 1 | 0 |
| *s<sub>163</sub>* | Curse | 1 | 0 |
| *s<sub>164</sub>* | Embargo | 1 | 0 |
| *s<sub>165</sub>* | Encore | 1 | 0 |
| *s<sub>166</sub>* | Heal Block | 1 | 0 |
| *s<sub>167</sub>* | Identified | 1 | 0 |
| *s<sub>168</sub>* | Infatuation | 1 | 0 |
| *s<sub>169</sub>* | Leech Seed | 1 | 0 |
| *s<sub>170</sub>* | Nightmare | 1 | 0 |
| *s<sub>171</sub>* | Perish Song | 1 | 0 |
| *s<sub>172</sub>* | Taunt | 1 | 0 |
| *s<sub>173</sub>* | Telekinesis | 1 | 0 |
| *s<sub>174</sub>* | Torment | 1 | 0 |
| *s<sub>175</sub>* | Aqua Ring | 1 | 0 |
| *s<sub>176</sub>* | Charging turn | 1 | 0 |
| *s<sub>177</sub>* | Defense Curl | 1 | 0 |
| *s<sub>178</sub>* | Rooting | 1 | 0 |
| *s<sub>179</sub>* | Magnetic levitation | 1 | 0 |
| *s<sub>180</sub>* | Recharging | 1 | 0 |
| *s<sub>181</sub>* | Semi-invulnerable | 1 | 0 |
| *s<sub>182</sub>* | Substitute | 1 | 0 |
| *s<sub>183</sub>* | Taking aim | 1 | 0 |
| *s<sub>184</sub>* | Withdrawing | 1 | 0 |

**Opponent's active pokemon (Status)**

| State | Description | Active | Inactive |
| :---: | :--- | :---: | :---: |
| *s<sub>185</sub>* | Bound | 1 | 0 |
| *s<sub>186</sub>* | Can't escape | 1 | 0 |
| *s<sub>187</sub>* | Confusion | 1 | 0 |
| *s<sub>188</sub>* | Curse | 1 | 0 |
| *s<sub>189</sub>* | Embargo | 1 | 0 |
| *s<sub>190</sub>* | Encore | 1 | 0 |
| *s<sub>191</sub>* | Heal Block | 1 | 0 |
| *s<sub>192</sub>* | Identified | 1 | 0 |
| *s<sub>193</sub>* | Infatuation | 1 | 0 |
| *s<sub>194</sub>* | Leech Seed | 1 | 0 |
| *s<sub>195</sub>* | Nightmare | 1 | 0 |
| *s<sub>196</sub>* | Perish Song | 1 | 0 |
| *s<sub>197</sub>* | Taunt | 1 | 0 |
| *s<sub>198</sub>* | Telekinesis | 1 | 0 |
| *s<sub>199</sub>* | Torment | 1 | 0 |
| *s<sub>200</sub>* | Aqua Ring | 1 | 0 |
| *s<sub>201</sub>* | Charging turn | 1 | 0 |
| *s<sub>202</sub>* | Defense Curl | 1 | 0 |
| *s<sub>203</sub>* | Rooting | 1 | 0 |
| *s<sub>204</sub>* | Magnetic levitation | 1 | 0 |
| *s<sub>205</sub>* | Recharging | 1 | 0 |
| *s<sub>206</sub>* | Semi-invulnerable | 1 | 0 |
| *s<sub>207</sub>* | Substitute | 1 | 0 |
| *s<sub>208</sub>* | Taking aim | 1 | 0 |
| *s<sub>209</sub>* | Withdrawing | 1 | 0 |

**Backups**

| State | Description | Active | Inactive |
| :---: | :--- | :---: | :---: |
| *s<sub>210</sub>* | backup1 | 1 | 0 |
| *s<sub>211</sub>* | backup2 | 1 | 0 |
| *s<sub>212</sub>* | backup3 | 1 | 0 |
| *s<sub>213</sub>* | backup4 | 1 | 0 |
| *s<sub>214</sub>* | backup5 | 1 | 0 |
| *s<sub>215</sub>* | backup6 | 1 | 0 |
| *s<sub>216</sub>* | backup7 | 1 | 0 |
| *s<sub>217</sub>* | backup8 | 1 | 0 |
| *s<sub>218</sub>* | backup9 | 1 | 0 |
| *s<sub>219</sub>* | backup10 | 1 | 0 |
| *s<sub>220</sub>* | backup11 | 1 | 0 |
| *s<sub>221</sub>* | backup12 | 1 | 0 |
| *s<sub>222</sub>* | backup13 | 1 | 0 |
| *s<sub>223</sub>* | backup14 | 1 | 0 |
| *s<sub>224</sub>* | backup15 | 1 | 0 |

Therefore, *n* = |**x**(*s*)| = 225

## **x**(*s*, *a*): vector of features visible when in state *s* taking action *a*
A common way to derive an action-feature vector **x**(*s*, *a*) from a state-feature vector **x**(*s*) involves an action-feature vector of size *n*|*A*|, where *n* is the number of state features and |*A*| is the number of actions. Each action corresponds with a block of *n* features in this action-feature vector. The features in **x**(*s*, *a*) that corresponds to action *a* take on the values of the state features; the features corresponding to other actions have a value of 0.

In a single state, by taking into account the possibilities of mega, zmove, ultra and switches, the total number of actions available is (4)(2) + 5 = **13**. On the other hand, the maximum action space for a standard team is (4)(6)(2) + 6 =**54**. Therefore, |*A*| = 54.

*n*|*A*| = (225)(54) = 12,150

Therefore, **x** outputs a vector with *d* = 12,150 such that **x**(*terminal*, *action*) = **0**.
