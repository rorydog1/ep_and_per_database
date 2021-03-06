#!/usr/local/bin/perl
use CGI::Pretty qw/:standard/;
use Mail::SendEasy;
#use Captcha::reCAPTCHA;

#my $c = Captcha::reCAPTCHA->new;

$email=param('email');
$email2=param('email2');
$message=param('message');
$to=param('to')||die 'no destination';
$subject=param('subject');
$name=param('name');
$inst=param('inst');
$journ=param('journ');
$refer=param('refer');
$verifytext=param('verifytext');
$challenge=param('recaptcha_challenge_field');
$response=param('recaptcha_response_field');
$quizz=param('quizz');
$quizz_ans=int( (param('quizz_ans'))/ 53);#We multiply by 53 to confuse clever spambots
if ($journ eq 'P'){$pubkey='6LcpxwAAAAAAALvPghTLwcJWGU-edxKrGJa5bi58'; $privkey='6LcpxwAAAAAAAJ7jokS9Hq32l28nzcRirNUFK2G5'}
elsif($journ=~/[A-D]/){
  $pubkey='6LfkxgAAAAAAALou3A9QZAMTKvqwjdAfFiaX4ijj'; $privkey='6LfkxgAAAAAAAH21msYa6CRw1tT07aul4FQ0W8ut'
}
elsif($jour eq 'H'){$pubkey='6LflxgAAAAAAAEpO12uWfXd52VBJg1yMH-nMbX0N'; $privkey='6LflxgAAAAAAAK8I2lxGnx3JEc-VNBYQw5p0-qrw'}
else {$pubkey='6LfixgAAAAAAAELRcfnOLvvA6_5IT2Xk5KAxIEmD'; $privkey='6LfixgAAAAAAAFsqiAYC1ftt-HatJ0WWnZVgov_O'}

#Question, answer, answer, answer, correct_answer (Fixed structure: 5 long, 3 rows, otherwise it will not work)
@quizz_questions=(
'What is one plus 1?',				'2',		'10',		'23',		'1',
'Is water wet or dry?',				'Dry',		'Wet',		'Both',		'2',
'Is Green a colour, sound or taste?',		'Taste',	'Sound',	'Colour',	'3'
);

#$pubkey='6LcpxwAAAAAAALvPghTLwcJWGU-edxKrGJa5bi58'; #$privkey='6LcpxwAAAAAAAJ7jokS9Hq32l28nzcRirNUFK2G5';

%destination=('webmaster','webmaster@pion.co.uk',
	      'sales','sales@pion.co.uk',
              'online','online@pion.co.uk',
              'permissions', 'permissions@pion.co.uk',
              'support', 'online@pion.co.uk',
	      'usage', 'online@pion.co.uk',
              'openurl', 'online@pion.co.uk',
              'Lesley Sackett', 'l.sackett@bristol.ac.uk',
              'Richard Gregory', 'l.sackett@bristol.ac.uk',
              'Suzanne McKee', 'suzanne@ski.org',
              'Peter Thompson', 'pt2@york.ac.uk',
              'Tom Troscianko', 'tom.troscianko@bris.ac.uk',
              'Christopher Tyler', 'cwt@ski.ski.org'
              );

 @weekDays = qw(Sun Mon Tue Wed Thu Fri Sat Sun);
($second, $minute, $hour, $dayOfMonth, $month, $yearOffset, $dayOfWeek, $dayOfYear, $daylightSavings) = localtime();
$thisyear = 1900 + $yearOffset;
$month++;


$refer=$ENV{'HTTP_REFERER'} unless $refer;

print header;
print start_html(-title=>'Contact Pion', -style=>'pion.css', -dtd=>'-//W3C//DTD HTML 4.0 Transitional//EN');

if($journ eq 'P'){
 print <<END;
<div id="header">
    <a href="P.html"><img src="Images/p_ban2.gif" alt="Perception" class="logo" /></a>

    <a href="http://www.pion.co.uk"><img src="Images/right_ban.gif" alt="Pion Ltd" class="pionlogo" /></a>
  </div>
  <div id="total">
    <div id="top-buttons">
      <div class="topnavigation">
	<ul>
	  <li><a href="search.cgi?journal=P." title="Search all papers">Search</a></li>
	  <li><a href="contents.cgi?journal=P&issue=current" title="View latest issue">Current&nbsp;issue</a></li>
	  <li><a href="contents.cgi?journal=P" title="View latest volume">Current&nbsp;volume</a></li>
	  <li><a href="contents.cgi?journal=P&volume=forthcoming" title="View forthcoming papers">Forthcoming</a></li>
	  <li><a href="allvols.cgi?journal=P" title="View all published volumes">All&nbsp;volumes</a></li>
	  <li><a href="index.html" title="Go to Perception homepage">Perception&nbsp;homepage</a></li>
          <li><a href="ECVP.html" title="ECVP abstracts">ECVP</a></li>
	  <li><a href="http://www.pion.co.uk" title="Go to Pion ltd homepage">Pion&nbsp;homepage</a></li>
	</ul>
      </div>
    </div>
    <div id="title">
      <font size=4>
	<div class="left">Contact <i>$to</i></div>
	<div class="center"></div>
	<div class="right"></div>

      </font>
    </div>
END
} elsif($journ eq 'X'| $journ eq 'E'| $journ eq 'A'| $journ eq 'B'| $journ eq 'C'| $journ eq 'D') {
 print <<END;
    <div id="header">
      <a href="index.html"><img src="Images/ep_ban.gif" alt="environment and planning" class="logo" /></a>
      <a href="http://www.pion.co.uk"><img src="Images/right_ban.gif" alt="Pion Ltd" class="pionlogo" /></a>
    </div>
    <div id="total">
      <div id="top-buttons">
	<div class="topnavigation">
	  <ul>
	    <li><a href="A.html" title="Go to Environment and Planning A homepage">EPA&nbsp;homepage</a></li>
	    <li><a href="B.html" title="Go to Environment and Planning B homepage">EPB&nbsp;homepage</a></li>
	    <li><a href="C.html" title="Go to Environment and Planning C homepage">EPC&nbsp;homepage</a></li>
	    <li><a href="D.html" title="Go to Environment and Planning D homepage">EPD&nbsp;homepage</a></li>
	    <li><a href="index.html" title="Go to Environment and Planning homepage">EP&nbsp;homepage</a></li>
	    <li><a href="http://www.pion.co.uk" title="Go to Pion ltd homepage">Pion&nbsp;homepage</a></li>
	  </ul>
	</div>
      </div>
      <div id="title">
      <font size=4>
	<div class="left">Contact <i>$to</i></div>
	<div class="center"></div>
	<div class="right"></div>

      </font>
    </div>
END
} else {
 print <<END;
   <div id="header">
      <a href="http://www.pion.co.uk"><img src="Images/pion_new2.gif" alt="Pion" class="logo"/></a>
      <a href="http://www.pion.co.uk"><img src="Images/right_ban.gif" alt="" class="pionlogo" /></a>
    </div>
    <div id="total">
      <div id="top-buttons">
	<div class="topnavigation">
	  <ul>
	    <li><a href="librarians.html" title="Information for librarians">For&nbsp;librarians</a></li>
	    <li><a href="contacts.html" title="Contact Pion">Pion&nbsp;contacts</a></li>
	    <li><a href="index.html" title="Go to Pion ltd homepage">Pion&nbsp;homepage</a></li>
	  </ul>
	</div>
      </div>
      <div id="title">
      <font size=4>
	<div class="left">Contact <i>$to</i></div>
	<div class="center"></div>
	<div class="right"></div>
      </font>
    </div>
END
}

#if($message =~ /<a href/ ||( $message=~/http:\/\// && $destination ne 'openurl')){
#  #assume this is spam!!
#  print p, "Sorry, could not deliver message", end_html;
#  exit;
#}



unless ($email&&$message){
  printform();
}
else {     
  
  #unless($refer=~/contact.cgi/){print p,"Sorry, unable to transmit message\n", end_html; exit}  

  #----------------------------------------------------------------------------------
  # this section based on check-captcha.cgi, see http://bumblebeeware.com/captcha/
  
  #$tempdir = "/htdocs/website/db/captchaTemp";
  ##if ($ENV{"REQUEST_METHOD"} ne "POST"){&nopost;}
  
  ## use this program to remove all old temp files
  ## this keeps the director clean without setting up a cron job
  #opendir TMPDIR, "$tempdir"; 
  #@alltmpfiles = readdir TMPDIR;
  #
  #foreach $oldtemp (@alltmpfiles) {
  #
  #        $age = 0;
  #        $age = (stat("$tempdir/$oldtemp"))[9];
  #        # if age is more than 300 seconds or 5 minutes	
  #        if ((time - $age) > 300){unlink "$tempdir/$oldtemp";}
  #        
  #        }
  #
  #
  ## open the temp datafile for current user based on ip
  #$tempfile = "$tempdir/$ENV{'REMOTE_ADDR'}";
  #open (TMPFILE, "<$tempfile")|| ($nofile = 1);
  #(@tmpfile) = <TMPFILE>;
  #close TMPFILE;
  
  ## if no matching ip file check for a cookie match
  ## this will compensate for AOL proxy servers accessing images
  ##if ($nofile == 1){
  ##	
  ##$cookieip = $ENV{HTTP_COOKIE};
  ##$cookieip =~ /checkme=([^;]*)/;
  ##$cookieip = $1;
  ##
  ##if ($cookieip ne ""){
  ##	
  ##	$tempfile = "$tempdir/$cookieip";
  ##	open (TMPFILE, "<$tempdir/$cookieip")|| &nofile;
  ##	(@tmpfile) = <TMPFILE>;
  ##	close TMPFILE;
  ##}
  #
  ##}
  #
  #$imagetext = $tmpfile[0];
  #chomp $imagetext;
  #
  ## set the form input to lower case
  #$verifytext = lc($verifytext);
  #
  ## compare the form input with the file text
  #if ($verifytext ne "$imagetext"){
  #  # now delete the temp file so it cannot be used again by the same user
  #  unlink "$tempdir/$ENV{'REMOTE_ADDR'}";
  #  &printform('The verification code does not match, please try again')}
  #
  ## now delete the temp file so it cannot be used again by the same user
  #unlink "$tempfile";
  #
  ## if no error continue with the program
  ##----------------------------------------------------------------------

   #Verify submission
#    my $result = $c->check_answer(
#        $privkey, $ENV{'REMOTE_ADDR'},
#        $challenge, $response
#    );

#    unless( $result->{is_valid} ) {$error = $result->{error};
#        &printform("The verification code does not match, please try again")}    

#print "quizz".int($quizz)."quizz_ans $quizz_ans quizz result ".int($quizz_questions[$quizz_ans]);  

      unless(int($quizz) == int($quizz_questions[$quizz_ans]) ){$error = $result->{error};
        &printform("Wrong answer to spam filter question, please try again")} 
#print "mail sent";
#die;
  if($email=~/^[a-zA-Z][\w\.-]*[a-zA-Z0-9]@[a-zA-Z0-9][\w\.-]*[a-zA-Z0-9]\.[a-zA-Z][a-zA-Z\.]*[a-zA-Z]$/ && $email eq $email2){
    #print "email ok";
    if ($destination{$to}){
      if ($message){
        #send email
        
        #$message="[Sent via Pion website]\nFrom: $name\n$inst\n\n$message";
        
        $mail = new Mail::SendEasy(smtp => 'mailgate.pion.ltd.uk');
        $status = $mail->send(
         from    => $email ,
         from_title => $name ,
         to      => $destination{$to} ,
         subject => "[via Pion website] $subject" ,
         msg     => "[Sent via Pion website]\nTo: $to\nFrom: $name <$email>, $inst\n(This email address has been entered manually by the sender)\n\n$message"
         )  ;
         #msgid   => "$pionid-$random"
 # ) ; #removed   html    => $html ,
  
#  print "<br>Message status: $status<br>";
      #print $mail->error;
      #print h1('Message sent');
      if($mail->error){
        $destination{$to}=~s/@/(AT)/;
        print h1('Problem sending message'), p, "We regret that a technical problem has prevented your message being sent, please send your message directly to $destination{$to}, replacing (AT) with an at-sign."}
      else {
        print h1('Message sent'), p, 'Thank you for your message';
        print p, "<a href='$refer'>Continue</a>"  if $refer;
      }
      print end_html; 
      } 
      else {
        printform('No message');
      }
    }
    else {
      printform('Bad destination');
    }
  }
  else {
    printform('The email address you have entered seems to have errors in it, please try again.');
  }
}


#print form, including any error message, and exit
sub printform {
  print h1("Contact <i>$to</i> at Pion") unless $journ;
  
  #print $ENV{'HTTP_REFERER'};
  
  print p,"<font color='red'>Error: $_[0]</font>",p if $_[0];
  $randomnumber=time;
  
#  $captcha=$c->get_html( $pubkey );
#Pick a quizz question and answer
$question		= int(rand(3))*5;
$q1		=$question +1;
$q2		=$question +2;
$q3		=$question +3;
$quizz_ans	=($question +4)*53;#Multiply by 53 to confuse clever spambots

  print <<END;
     <div class="space"></div>
<form action="contact.cgi" method="post">
<input type="hidden" name="to" value="$to"><input type="hidden" name="refer" value="$refer">
<input type="hidden" name="journ" value="$journ">
<input type="hidden" name="quizz_ans" value="$quizz_ans">
Please enter your name:<br>
<input type="text" name="name" value="$name"><br>
Institution (if applicable):<br>
<input type="text" name="inst" value="$inst"><br>
Email address (please enter this carefully as we will need it to reply to you):<br>
<input type="text" name="email" value="$email"><br>
Please enter your email address again for confirmation:<br>
<input type="text" name="email2" value="$email2">
<p>Subject:<br>
<input type="text" name="subject" size=80 value="$subject">
<p>Message:
<br><textarea name="message" cols="80" rows="16" size="5000">$message</textarea>
<p>Please answer the following question:
<p>$quizz_questions[$question]</p>
<p></p>
$quizz_questions[$q1]<input type="radio" name="quizz" value="1" /><br />
$quizz_questions[$q2]<input type="radio" name="quizz" value="2" /><br />
$quizz_questions[$q3]<input type="radio" name="quizz" value="3" /><br />
<p><input type="submit" value="Send message">
</form>
    <div class="space"></div>
    <div id="footer">
	<div class="right">Copyright &copy; $thisyear a <a href="http://www.pion.co.uk">Pion</a> publication.</div>
    </div>
END
  print end_html;
  exit;
}

sub nopost {
	
#print "Content-type: text/html\n\n";
print "method not allowed, input must be via a form post.";	
exit;	
}

sub nofile {
	
#print "Content-type: text/html\n\n";
print "no file found for verification.";	
exit;	
}
