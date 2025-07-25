from openai import OpenAI
from decouple import config

contents = '''
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8"/>
	<title></title>
	<meta name="generator" content="LibreOffice 25.2.4.3 (MacOSX)"/>
	<meta name="created" content="00:00:00"/>
	<meta name="changed" content="00:00:00"/>
	<style type="text/css">
		@page { size: 21.59cm 27.94cm; margin-left: 3.18cm; margin-right: 3.18cm; margin-top: 2.54cm; margin-bottom: 2.54cm }
		p { direction: ltr; widows: 2; orphans: 2; margin-bottom: 0.25cm; page-break-inside: auto; text-align: left; line-height: 115%; background: transparent; page-break-after: auto }
		h1 { direction: ltr; margin-bottom: 0cm; orphans: 2; text-align: left; page-break-inside: auto; widows: 2; line-height: 108%; color: #2f5496; background: transparent; page-break-after: auto }
		h1.western { font-size: 16pt; font-family: "Calibri Light", serif }
		h1.cjk { font-size: 16pt }
		h2 { direction: ltr; margin-top: 0.07cm; margin-bottom: 0cm; orphans: 2; text-align: left; page-break-inside: auto; widows: 2; line-height: 108%; color: #2f5496; background: transparent; page-break-after: auto }
		h2.western { font-size: 13pt; font-family: "Calibri Light", serif }
		h2.cjk { font-size: 13pt }
		h3 { direction: ltr; margin-top: 0.07cm; margin-bottom: 0cm; orphans: 2; text-align: left; page-break-inside: auto; widows: 2; line-height: 108%; color: #1f3763; background: transparent; page-break-after: auto }
		h3.western { font-size: 12pt; font-family: "Calibri Light", serif }
		h3.cjk { font-size: 12pt }
		a:link { color: #000080; text-decoration: underline }
	</style>
</head>
<body lang="en-GB" link="#000080" vlink="#800000" bgcolor="#ffffff" dir="ltr">
<div id="Table of Contents1" dir="ltr"><p style="line-height: 100%; margin-bottom: 0.18cm">
	<a href="#_Toc000000001"><span style="text-decoration: none"><font face="Calibri, serif"><span style="font-style: normal"><b>Technology:
	A Comprehensive Report</b></span></font></span>	1</a></p>
	<p style="line-height: 100%; margin-bottom: 0.18cm; margin-left: 0.39cm">
	<a href="#_Toc000000002"><span style="text-decoration: none"><font face="Times New Roman, serif"><span style="font-style: normal"><b>1.
	Introduction</b></span></font></span>	1</a></p>
	<p style="line-height: 100%; margin-bottom: 0.18cm; margin-left: 0.39cm">
	<a href="#_Toc000000003"><span style="text-decoration: none"><font face="Times New Roman, serif"><span style="font-style: normal"><b>2.
	Historical Evolution of Technology</b></span></font></span>	2</a></p>
	<p style="line-height: 100%; margin-bottom: 0.18cm; margin-left: 0.78cm">
	<a href="#_Toc000000004"><span style="text-decoration: none"><font face="Times New Roman, serif"><span style="font-style: normal"><b>2.1
	Ancient Innovations</b></span></font></span>	2</a></p>
	<p style="line-height: 100%; margin-bottom: 0.18cm; margin-left: 0.78cm">
	<a href="#_Toc000000005"><span style="text-decoration: none"><font face="Times New Roman, serif"><span style="font-style: normal"><b>2.2
	Industrial Revolution</b></span></font></span>	2</a></p>
	<p style="line-height: 100%; margin-bottom: 0.18cm; margin-left: 0.78cm">
	<a href="#_Toc000000006"><span style="text-decoration: none"><font face="Times New Roman, serif"><span style="font-style: normal"><b>2.3
	Digital Revolution</b></span></font></span>	2</a></p>
	<p style="line-height: 100%; margin-bottom: 0.18cm; margin-left: 0.39cm">
	<a href="#_Toc000000007"><span style="text-decoration: none"><font face="Times New Roman, serif"><span style="font-style: normal"><b>3.
	Key Areas of Technological Advancement</b></span></font></span>	2</a></p>
	<p style="line-height: 100%; margin-bottom: 0.18cm; margin-left: 0.78cm">
	<a href="#_Toc000000008"><span style="text-decoration: none"><font face="Times New Roman, serif"><span style="font-style: normal"><b>3.1
	Information and Communication Technology (ICT)</b></span></font></span>	2</a></p>
	<p style="line-height: 100%; margin-bottom: 0.18cm; margin-left: 0.78cm">
	<a href="#_Toc000000009"><span style="text-decoration: none"><font face="Times New Roman, serif"><span style="font-style: normal"><b>3.2
	Artificial Intelligence and Machine Learning</b></span></font></span>	2</a></p>
	<p style="line-height: 100%; margin-bottom: 0.18cm; margin-left: 0.78cm">
	<a href="#_Toc000000010"><span style="text-decoration: none"><font face="Times New Roman, serif"><span style="font-style: normal"><b>3.3
	Biotechnology</b></span></font></span>	2</a></p>
	<p style="line-height: 100%; margin-bottom: 0.18cm; margin-left: 0.78cm">
	<a href="#_Toc000000011"><span style="text-decoration: none"><font face="Times New Roman, serif"><span style="font-style: normal"><b>3.4
	Renewable Energy</b></span></font></span>	2</a></p>
	<p style="line-height: 100%; margin-bottom: 0.18cm; margin-left: 0.78cm">
	<a href="#_Toc000000012"><span style="text-decoration: none"><font face="Times New Roman, serif"><span style="font-style: normal"><b>3.5
	Robotics and Automation</b></span></font></span>	2</a></p>
	<p style="line-height: 100%; margin-bottom: 0.18cm; margin-left: 0.39cm">
	<a href="#_Toc000000013"><span style="text-decoration: none"><font face="Times New Roman, serif"><span style="font-style: normal"><b>4.
	Impact of Technology on Society</b></span></font></span>	2</a></p>
	<p style="line-height: 100%; margin-bottom: 0.18cm; margin-left: 0.78cm">
	<a href="#_Toc000000014"><span style="text-decoration: none"><font face="Times New Roman, serif"><span style="font-style: normal"><b>4.1
	Positive Impacts</b></span></font></span>	2</a></p>
	<p style="line-height: 100%; margin-bottom: 0.18cm; margin-left: 0.78cm">
	<a href="#_Toc000000015"><span style="text-decoration: none"><font face="Times New Roman, serif"><span style="font-style: normal"><b>4.2
	Negative Impacts</b></span></font></span>	3</a></p>
	<p style="line-height: 100%; margin-bottom: 0.18cm; margin-left: 0.39cm">
	<a href="#_Toc000000016"><span style="text-decoration: none"><font face="Times New Roman, serif"><span style="font-style: normal"><b>5.
	Future Trends in Technology</b></span></font></span>	3</a></p>
	<p style="line-height: 100%; margin-bottom: 0.18cm; margin-left: 0.78cm">
	<a href="#_Toc000000017"><span style="text-decoration: none"><font face="Times New Roman, serif"><span style="font-style: normal"><b>5.1
	Quantum Computing</b></span></font></span>	3</a></p>
	<p style="line-height: 100%; margin-bottom: 0.18cm; margin-left: 0.78cm">
	<a href="#_Toc000000018"><span style="text-decoration: none"><font face="Times New Roman, serif"><span style="font-style: normal"><b>5.2
	Internet of Things (IoT)</b></span></font></span>	3</a></p>
	<p style="line-height: 100%; margin-bottom: 0.18cm; margin-left: 0.78cm">
	<a href="#_Toc000000019"><span style="text-decoration: none"><font face="Times New Roman, serif"><span style="font-style: normal"><b>5.3
	Extended Reality (XR)</b></span></font></span>	3</a></p>
	<p style="line-height: 100%; margin-bottom: 0.18cm; margin-left: 0.78cm">
	<a href="#_Toc000000020"><span style="text-decoration: none"><font face="Times New Roman, serif"><span style="font-style: normal"><b>5.4
	Ethical AI and Tech Regulation</b></span></font></span>	3</a></p>
	<p style="line-height: 100%; margin-bottom: 0.18cm; margin-left: 0.39cm">
	<a href="#_Toc000000021"><span style="text-decoration: none"><font face="Times New Roman, serif"><span style="font-style: normal"><b>6.
	Conclusion</b></span></font></span>	4</a></p>
</div>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
<p align="left" style="font-variant: normal; widows: 2; font-weight: normal; font-style: normal; orphans: 2; page-break-inside: auto; border: none; padding: 0cm; line-height: 0.42cm; margin-bottom: 0.21cm; text-decoration: none; page-break-after: auto">
<br/>
<br/>

</p>
<h1 class="western" align="left" style="widows: 2; line-height: 0.42cm; page-break-inside: avoid; border: none; padding: 0cm; orphans: 2; margin-top: 0.85cm; margin-bottom: 0.21cm; page-break-after: avoid"><a name="_Toc000000001"></a>
<span style="font-variant: normal"><font color="#ff0000"><span style="text-decoration: none"><font face="Calibri, serif"><font size="6" style="font-size: 24pt">Technology:
A Comprehensive Report</font></font></span></font></span></h1>
<p align="left" style="widows: 2; border: none; padding: 0cm; orphans: 2; line-height: 0.42cm; page-break-inside: auto; margin-bottom: 0cm; page-break-after: auto">
<span style="font-variant: normal"><span style="text-decoration: none"><font face="Times New Roman, serif"><font size="2" style="font-size: 11pt"><br/>
</font></font></span></span><br/>

</p>
<h2 class="western" align="left" style="widows: 2; line-height: 0.42cm; page-break-inside: avoid; border: none; padding: 0cm; orphans: 2; margin-top: 0.64cm; margin-bottom: 0.14cm; page-break-after: avoid"><a name="_Toc000000002"></a>
<span style="font-variant: normal"><font color="#ff0000"><span style="text-decoration: none"><font face="Arial, serif"><font size="5" style="font-size: 18pt">1.
Introduction</font></font></span></font></span></h2>
<p align="left" style="widows: 2; border: none; padding: 0cm; orphans: 2; line-height: 0.42cm; page-break-inside: auto; margin-bottom: 0cm; page-break-after: auto">
<span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt">Technology
refers to the application of scientific knowledge for practical
purposes. From the invention of the wheel to artificial intelligence,
technology has consistently shaped human civilization. In the 21st
century, it influences every sector—from communication to
healthcare. This report explores the evolution, trends, and
implications of technology.</font></font></span></span></p>
<h2 class="western" align="left" style="widows: 2; line-height: 0.42cm; page-break-inside: avoid; border: none; padding: 0cm; orphans: 2; margin-top: 0.64cm; margin-bottom: 0.14cm; page-break-after: avoid"><a name="_Toc000000003"></a>
<span style="font-variant: normal"><font color="#ff0000"><span style="text-decoration: none"><font face="Arial, serif"><font size="5" style="font-size: 18pt">2.
Historical Evolution of Technology</font></font></span></font></span></h2>
<h3 class="western" align="left" style="widows: 2; line-height: 0.42cm; page-break-inside: avoid; border: none; padding: 0cm; orphans: 2; margin-top: 0.49cm; margin-bottom: 0.14cm; page-break-after: avoid"><a name="_Toc000000004"></a>
<span style="font-variant: normal"><font color="#ff0000"><span style="text-decoration: none"><font face="Arial, serif"><font size="4" style="font-size: 14pt">2.1
Ancient Innovations</font></font></span></font></span></h3>
<p align="left" style="widows: 2; border: none; padding: 0cm; orphans: 2; line-height: 0.42cm; page-break-inside: auto; margin-bottom: 0cm; page-break-after: auto">
<span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt">Early
humans created tools from stone and wood. The agricultural revolution
brought irrigation systems and plows.</font></font></span></span></p>
<h3 class="western" align="left" style="widows: 2; line-height: 0.42cm; page-break-inside: avoid; border: none; padding: 0cm; orphans: 2; margin-top: 0.49cm; margin-bottom: 0.14cm; page-break-after: avoid"><a name="_Toc000000005"></a>
<span style="font-variant: normal"><font color="#ff0000"><span style="text-decoration: none"><font face="Arial, serif"><font size="4" style="font-size: 14pt">2.2
Industrial Revolution</font></font></span></font></span></h3>
<p align="left" style="widows: 2; border: none; padding: 0cm; orphans: 2; line-height: 0.42cm; page-break-inside: auto; margin-bottom: 0cm; page-break-after: auto">
<span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt">The
18th–19th centuries saw mechanization via steam engines and
electricity, transforming production and transportation.</font></font></span></span></p>
<h3 class="western" align="left" style="widows: 2; line-height: 0.42cm; page-break-inside: avoid; border: none; padding: 0cm; orphans: 2; margin-top: 0.49cm; margin-bottom: 0.14cm; page-break-after: avoid"><a name="_Toc000000006"></a>
<span style="font-variant: normal"><font color="#ff0000"><span style="text-decoration: none"><font face="Arial, serif"><font size="4" style="font-size: 14pt">2.3
Digital Revolution</font></font></span></font></span></h3>
<p align="left" style="widows: 2; border: none; padding: 0cm; orphans: 2; line-height: 0.42cm; page-break-inside: auto; margin-bottom: 0cm; page-break-after: auto">
<span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt">Computers,
the internet, and mobile devices reshaped communication and laid the
foundation for today’s digital age.</font></font></span></span></p>
<h2 class="western" align="left" style="widows: 2; line-height: 0.42cm; page-break-inside: avoid; border: none; padding: 0cm; orphans: 2; margin-top: 0.64cm; margin-bottom: 0.14cm; page-break-after: avoid"><a name="_Toc000000007"></a>
<span style="font-variant: normal"><font color="#ff0000"><span style="text-decoration: none"><font face="Arial, serif"><font size="5" style="font-size: 18pt">3.
Key Areas of Technological Advancement</font></font></span></font></span></h2>
<h3 class="western" align="left" style="widows: 2; line-height: 0.42cm; page-break-inside: avoid; border: none; padding: 0cm; orphans: 2; margin-top: 0.49cm; margin-bottom: 0.14cm; page-break-after: avoid"><a name="_Toc000000008"></a>
<span style="font-variant: normal"><font color="#ff0000"><span style="text-decoration: none"><font face="Arial, serif"><font size="4" style="font-size: 14pt">3.1
Information and Communication Technology (ICT)</font></font></span></font></span></h3>
<p align="left" style="widows: 2; border: none; padding: 0cm; orphans: 2; line-height: 0.42cm; page-break-inside: auto; margin-bottom: 0cm; page-break-after: auto">
<span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt">ICT
encompasses computers, smartphones, networks, and software, enabling
global connectivity.</font></font></span></span></p>
<h3 class="western" align="left" style="widows: 2; line-height: 0.42cm; page-break-inside: avoid; border: none; padding: 0cm; orphans: 2; margin-top: 0.49cm; margin-bottom: 0.14cm; page-break-after: avoid"><a name="_Toc000000009"></a>
<span style="font-variant: normal"><font color="#ff0000"><span style="text-decoration: none"><font face="Arial, serif"><font size="4" style="font-size: 14pt">3.2
Artificial Intelligence and Machine Learning</font></font></span></font></span></h3>
<p align="left" style="widows: 2; border: none; padding: 0cm; orphans: 2; line-height: 0.42cm; page-break-inside: auto; margin-bottom: 0cm; page-break-after: auto">
<span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt">AI
enables machines to mimic human intelligence, impacting industries
with applications like virtual assistants and autonomous vehicles.</font></font></span></span></p>
<h3 class="western" align="left" style="widows: 2; line-height: 0.42cm; page-break-inside: avoid; border: none; padding: 0cm; orphans: 2; margin-top: 0.49cm; margin-bottom: 0.14cm; page-break-after: avoid"><a name="_Toc000000010"></a>
<span style="font-variant: normal"><font color="#ff0000"><span style="text-decoration: none"><font face="Arial, serif"><font size="4" style="font-size: 14pt">3.3
Biotechnology</font></font></span></font></span></h3>
<p align="left" style="widows: 2; border: none; padding: 0cm; orphans: 2; line-height: 0.42cm; page-break-inside: auto; margin-bottom: 0cm; page-break-after: auto">
<span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt">Gene
editing, sequencing, and synthetic biology revolutionize healthcare,
agriculture, and environmental science.</font></font></span></span></p>
<h3 class="western" align="left" style="widows: 2; line-height: 0.42cm; page-break-inside: avoid; border: none; padding: 0cm; orphans: 2; margin-top: 0.49cm; margin-bottom: 0.14cm; page-break-after: avoid"><a name="_Toc000000011"></a>
<span style="font-variant: normal"><font color="#ff0000"><span style="text-decoration: none"><font face="Arial, serif"><font size="4" style="font-size: 14pt">3.4
Renewable Energy</font></font></span></font></span></h3>
<p align="left" style="widows: 2; border: none; padding: 0cm; orphans: 2; line-height: 0.42cm; page-break-inside: auto; margin-bottom: 0cm; page-break-after: auto">
<span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt">Solar,
wind, and hydroelectric energy reduce dependence on fossil fuels and
combat climate change.</font></font></span></span></p>
<h3 class="western" align="left" style="widows: 2; line-height: 0.42cm; page-break-inside: avoid; border: none; padding: 0cm; orphans: 2; margin-top: 0.49cm; margin-bottom: 0.14cm; page-break-after: avoid"><a name="_Toc000000012"></a>
<span style="font-variant: normal"><font color="#ff0000"><span style="text-decoration: none"><font face="Arial, serif"><font size="4" style="font-size: 14pt">3.5
Robotics and Automation</font></font></span></font></span></h3>
<p align="left" style="widows: 2; border: none; padding: 0cm; orphans: 2; line-height: 0.42cm; page-break-inside: auto; margin-bottom: 0cm; page-break-after: auto">
<span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt">Automation
is growing in manufacturing and services. Robots perform tasks in
surgeries, warehouses, and customer service.</font></font></span></span></p>
<h2 class="western" align="left" style="widows: 2; line-height: 0.42cm; page-break-inside: avoid; border: none; padding: 0cm; orphans: 2; margin-top: 0.64cm; margin-bottom: 0.14cm; page-break-after: avoid"><a name="_Toc000000013"></a>
<span style="font-variant: normal"><font color="#ff0000"><span style="text-decoration: none"><font face="Arial, serif"><font size="5" style="font-size: 18pt">4.
Impact of Technology on Society</font></font></span></font></span></h2>
<h3 class="western" align="left" style="widows: 2; line-height: 0.42cm; page-break-inside: avoid; border: none; padding: 0cm; orphans: 2; margin-top: 0.49cm; margin-bottom: 0.14cm; page-break-after: avoid"><a name="_Toc000000014"></a>
<span style="font-variant: normal"><font color="#ff0000"><span style="text-decoration: none"><font face="Arial, serif"><font size="4" style="font-size: 14pt">4.1
Positive Impacts</font></font></span></font></span></h3>
<p align="left" style="widows: 2; border: none; padding: 0cm; orphans: 2; line-height: 0.42cm; page-break-inside: auto; margin-bottom: 0cm; page-break-after: auto">
<span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt">Technology
improves communication, healthcare, education, and drives economic
growth and innovation.</font></font></span></span></p>
<h3 class="western" align="left" style="widows: 2; line-height: 0.42cm; page-break-inside: avoid; border: none; padding: 0cm; orphans: 2; margin-top: 0.49cm; margin-bottom: 0.14cm; page-break-after: avoid"><a name="_Toc000000015"></a>
<span style="font-variant: normal"><font color="#ff0000"><span style="text-decoration: none"><font face="Arial, serif"><font size="4" style="font-size: 14pt">4.2
Negative Impacts</font></font></span></font></span></h3>
<p align="left" style="widows: 2; border: none; padding: 0cm; orphans: 2; line-height: 0.42cm; page-break-inside: auto; margin-bottom: 0cm; page-break-after: auto">
<span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt">While
technology offers numerous benefits, it also introduces significant
challenges and concerns that warrant careful consideration. These
include fundamental issues such as </font></font></span></span><span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt"><b>data
privacy</b></font></font></span></span><span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt">,
the potential for widespread </font></font></span></span><span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt"><b>job
displacement</b></font></font></span></span><span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt">
due to increasing automation, and the exacerbation of </font></font></span></span><span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt"><b>digital
inequality</b></font></font></span></span><span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt">,
which creates a divide between those with access to technology and
those without. Beyond these, there are growing concerns about the
</font></font></span></span><span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt"><b>mental
health impacts</b></font></font></span></span><span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt">
of constant connectivity and social media use. Addressing these
negative consequences is crucial for ensuring technology develops
responsibly and inclusively. Additional points of concern include:</font></font></span></span></p>
<ul>
	<li><p align="left" style="widows: 2; border: none; padding: 0cm; orphans: 2; line-height: 0.42cm; page-break-inside: auto; margin-bottom: 0cm; page-break-after: auto">
	<span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt"><b>Cybersecurity
	Risks</b></font></font></span></span><span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt">:
	The increasing reliance on digital systems makes individuals,
	businesses, and governments vulnerable to cyberattacks, data
	breaches, and identity theft.</font></font></span></span></p></li>
	<li><p align="left" style="widows: 2; border: none; padding: 0cm; orphans: 2; line-height: 0.42cm; page-break-inside: auto; margin-bottom: 0cm; page-break-after: auto">
	<span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt"><b>Ethical
	Dilemmas in AI</b></font></font></span></span><span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt">:
	As AI becomes more sophisticated, questions arise regarding
	algorithmic bias, accountability for AI decisions, and the potential
	for autonomous systems to operate without sufficient human
	oversight.</font></font></span></span></p></li>
	<li><p align="left" style="widows: 2; border: none; padding: 0cm; orphans: 2; line-height: 0.42cm; page-break-inside: auto; margin-bottom: 0cm; page-break-after: auto">
	<span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt"><b>Environmental
	Impact</b></font></font></span></span><span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt">:
	The production, use, and disposal of electronic devices contribute
	to e-waste, energy consumption, and the depletion of natural
	resources, posing significant environmental challenges.</font></font></span></span></p></li>
	<li><p align="left" style="widows: 2; border: none; padding: 0cm; orphans: 2; line-height: 0.42cm; page-break-inside: auto; margin-bottom: 0cm; page-break-after: auto">
	<span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt"><b>Misinformation
	and Disinformation</b></font></font></span></span><span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt">:
	Digital platforms can amplify the spread of false or misleading
	information, impacting public discourse, social cohesion, and
	democratic processes.</font></font></span></span></p></li>
	<li><p align="left" style="widows: 2; border: none; padding: 0cm; orphans: 2; line-height: 0.42cm; page-break-inside: auto; margin-bottom: 0cm; page-break-after: auto">
	<span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt"><b>Erosion
	of Human Connection</b></font></font></span></span><span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt">:
	Over-reliance on digital communication can sometimes diminish
	face-to-face interactions and foster feelings of isolation.</font></font></span></span></p></li>
	<li><p align="left" style="widows: 2; border: none; padding: 0cm; orphans: 2; line-height: 0.42cm; page-break-inside: auto; margin-bottom: 0cm; page-break-after: auto">
	<span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt"><b>Privacy
	and Surveillance</b></font></font></span></span><span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt">:
	The vast amounts of data collected by technological platforms raise
	concerns about surveillance, individual privacy, and the potential
	for misuse of personal information.</font></font></span></span></p></li>
</ul>
<h2 class="western" align="left" style="widows: 2; line-height: 0.42cm; page-break-inside: avoid; border: none; padding: 0cm; orphans: 2; margin-top: 0.64cm; margin-bottom: 0.14cm; page-break-after: avoid"><a name="_Toc000000016"></a>
<span style="font-variant: normal"><font color="#ff0000"><span style="text-decoration: none"><font face="Arial, serif"><font size="5" style="font-size: 18pt">5.
Future Trends in Technology</font></font></span></font></span></h2>
<h3 class="western" align="left" style="widows: 2; line-height: 0.42cm; page-break-inside: avoid; border: none; padding: 0cm; orphans: 2; margin-top: 0.49cm; margin-bottom: 0.14cm; page-break-after: avoid"><a name="_Toc000000017"></a>
<span style="font-variant: normal"><font color="#ff0000"><span style="text-decoration: none"><font face="Arial, serif"><font size="4" style="font-size: 14pt">5.1
Quantum Computing</font></font></span></font></span></h3>
<p align="left" style="widows: 2; border: none; padding: 0cm; orphans: 2; line-height: 0.42cm; page-break-inside: auto; margin-bottom: 0cm; page-break-after: auto">
<span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt">Quantum
computers will revolutionize data processing, cryptography, and
simulations.</font></font></span></span></p>
<h3 class="western" align="left" style="widows: 2; line-height: 0.42cm; page-break-inside: avoid; border: none; padding: 0cm; orphans: 2; margin-top: 0.49cm; margin-bottom: 0.14cm; page-break-after: avoid"><a name="_Toc000000018"></a>
<span style="font-variant: normal"><font color="#ff0000"><span style="text-decoration: none"><font face="Arial, serif"><font size="4" style="font-size: 14pt">5.2
Internet of Things (IoT)</font></font></span></font></span></h3>
<p align="left" style="widows: 2; border: none; padding: 0cm; orphans: 2; line-height: 0.42cm; page-break-inside: auto; margin-bottom: 0cm; page-break-after: auto">
<span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt">IoT
links devices across homes, industries, and cities, enhancing
automation and monitoring.</font></font></span></span></p>
<h3 class="western" align="left" style="widows: 2; line-height: 0.42cm; page-break-inside: avoid; border: none; padding: 0cm; orphans: 2; margin-top: 0.49cm; margin-bottom: 0.14cm; page-break-after: avoid"><a name="_Toc000000019"></a>
<span style="font-variant: normal"><font color="#ff0000"><span style="text-decoration: none"><font face="Arial, serif"><font size="4" style="font-size: 14pt">5.3
Extended Reality (XR)</font></font></span></font></span></h3>
<p align="left" style="widows: 2; border: none; padding: 0cm; orphans: 2; line-height: 0.42cm; page-break-inside: auto; margin-bottom: 0cm; page-break-after: auto">
<span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt">VR,
AR, and MR are transforming education, training, and entertainment
experiences.</font></font></span></span></p>
<h3 class="western" align="left" style="widows: 2; line-height: 0.42cm; page-break-inside: avoid; border: none; padding: 0cm; orphans: 2; margin-top: 0.49cm; margin-bottom: 0.14cm; page-break-after: avoid"><a name="_Toc000000020"></a>
<span style="font-variant: normal"><font color="#ff0000"><span style="text-decoration: none"><font face="Times New Roman, serif"><font size="4" style="font-size: 14pt">5.4
Ethical AI and Tech Regulation</font></font></span></font></span></h3>
<p align="left" style="widows: 2; border: none; padding: 0cm; orphans: 2; line-height: 0.42cm; page-break-inside: auto; margin-bottom: 0cm; page-break-after: auto">
<span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt">Responsible
AI use requires transparency, fairness, and international regulation
to prevent harm.</font></font></span></span></p>
<h2 class="western" align="left" style="widows: 2; line-height: 0.42cm; page-break-inside: avoid; border: none; padding: 0cm; orphans: 2; margin-top: 0.64cm; margin-bottom: 0.14cm; page-break-after: avoid"><a name="_Toc000000021"></a>
<span style="font-variant: normal"><font color="#ff0000"><span style="text-decoration: none"><font face="Arial, serif"><font size="5" style="font-size: 18pt">6.
Conclusion</font></font></span></font></span></h2>
<p align="left" style="widows: 2; border: none; padding: 0cm; orphans: 2; line-height: 0.42cm; page-break-inside: auto; margin-bottom: 0cm; page-break-after: auto">
<span style="font-variant: normal"><span style="text-decoration: none"><font face="Arial, serif"><font size="2" style="font-size: 11pt">Technology
presents both opportunity and risk. Collaboration and ethical
governance are essential to ensure inclusive and sustainable
development.</font></font></span></span></p>
<p align="left" style="widows: 2; border: none; padding: 0cm; orphans: 2; line-height: 100%; page-break-inside: auto; margin-bottom: 0cm; page-break-after: auto">
<span style="font-variant: normal"><span style="text-decoration: none"><font face="Times New Roman, serif"><font size="2" style="font-size: 11pt"><br/>
</font></font></span></span><br/>

</p>
<p style="line-height: 100%; margin-bottom: 0cm"><br/>

</p>
</body>
</html>
'''

client = OpenAI(
            api_key=config("GEMINI_API_KEY"),
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )
contents_list = [contents[i:i+500] for i in range(0, len(contents), 500)]

messages = [
    {
        "role": "system",
        "content": '''
        You are a helpful assistant of a word document. 
        The document will be passed as html and you are meant to edit it with html too.
        Use html tags to edit the document.
        Make sure to always return the html code.
        Must use inline styles always in class attribute.
        For line heights, do not use percentage.
        Use Px instead of CMs
        remove any style tags from the document and keep all styles in line
        '''
    }
]

for content in contents_list:
    messages.append({
        "role": "user",
        "content": content
    })

messages.append({
    "role": "user",
    "content": "Change all the headings to blue instead of red"
})

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=messages
)

print(response.choices[0].message.content)