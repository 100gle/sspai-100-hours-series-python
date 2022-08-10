from django.http import HttpResponse


def poem(request):

    content = """
    <style>
      figure {
        display: block;
        margin: auto;
        width: 40%;
      }
      figure > figcaption {
        text-align: center;
      }
      blockquote {
        margin: 0;
      }

      blockquote p {
        padding: 15px;
        line-height: 1cm;
        background: #eee;
        border-radius: 5px;
      }
    </style>
    <figure>
      <blockquote>
        <i>
          <p>
            Beautiful is better than ugly.<br />
            Explicit is better than implicit.<br />
            Simple is better than complex.<br />
            Complex is better than complicated.<br />
            Flat is better than nested.<br />
            Sparse is better than dense.<br />
            Readability counts.<br />
            Special cases aren't special enough to break the rules.<br />
            Although practicality beats purity.<br />
            Errors should never pass silently.<br />
            Unless explicitly silenced.<br />
            In the face of ambiguity, refuse the temptation to guess.<br />
            There should be one-- and preferably only one --obvious way to do
            it.<br />
            Although that way may not be obvious at first unless you're
            Dutch.<br />
            Now is better than never.<br />
            Although never is often better than *right* now.<br />
            If the implementation is hard to explain, it's a bad idea.<br />
            If the implementation is easy to explain, it may be a good idea.<br />
            Namespaces are one honking great idea -- let's do more of those!<br />
          </p>
        </i>
      </blockquote>
      <figcaption>
        ——Tim Peters, <cite><b>The Zen of Python</b></cite>
      </figcaption>
    </figure>
    """

    return HttpResponse(content)
