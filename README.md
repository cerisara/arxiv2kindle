Assuming that you have a number of references of arXiv papers disseminated in
text files within a known directory, this little script will:

- retrieve the arXiv paper ID from within your text files
- download their latex source (when available)
- convert (and not compile !) the latex into markdown
- convert the markdown to epub and then mobi

If you want to know how you can get the original text file with arXiv
references, I recommend you to have a look at my [tasklab](https://github.com/cerisara/tasklab) Android app, which gives you a one-click option to add such
references into a cloud-synchronized text file when browsing the web or Twitter.

This arxiv2kindle script does not compile the latex files: such
purely automated compilation may often fail, because of requirements of specific libraries
for instance. Also, there are several papers which latex source only loads
a unique big PDF and keep their code in a *comment* section, I guess when
latex compilation is too complex.

I have tried another option: extracting the text from the PDF, but it is
really crappy to read on Kindle because of broken line and paragraph segmentation, or worst equations and tables that are spread over several nearly blank
pages.

So I've chosen an intermediary solution: a simple (tunable) parsing of the latex source
into markdown. This parsing is really dumb, but it works without relying
on any latex library, and it at least creates a
nice-looking text with correct paragraph segmentations and section titles.
Most pictures should also be correctly inserted (although the script may be
improved for pictures).
Small-sized inline equations inside text, typically greek letters / parameters
definitions, are correctly rendered.
Longer equations are just printed out in their latex form, as well as tables.
This makes reading long equations and tables not so easy, but at least,
all the information is packed into a single paragraph and not spread over
multiple blank pages.
References are not handled.

Although this script is still far from perfect, and fails for instance to
get papers without latex sources, or pictures compiled with fancy
gnuplot/latex integrations, or pictures drawn inline with Tikz,
it is, as far as I know, the best looking output on Kindle for rendering
arXiv scientific papers.
And because it's very simple, it's straightforward to tune it and improve it
by yourself.

May be one day researchers will at least write papers directly in (enhanced)
Markdown, which will be much better for online, tablet, smartphone, kindle reading. But until then, this script is the only solution I've found so far to
carry with me a bunch or papers that I have had not the time to read yet when traveling. If you are aware of other options, please let me know !

Other scripts you may be interested in:

- [arxiv2kindle](https://gist.github.com/bshillingford/6259986edca707ca58dd)
- [arxiv2mobi](http://knanagnostopoulos.blogspot.fr/2013/03/from-arxiv-directly-to-my-kindle_15.html) : part of my script is taken from this blog.

