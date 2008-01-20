# NOTE
# - easy way to update all sources with new/old locales:
#   lynx -dump ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n | awk '/.tar.bz2$/{printf("Source%d: %s\n", i++, $2)}' | tee out
#   and then :r out in vim and ./builder -a5 the spec

%define		_state		stable
%define		_minlibsevr	9:%{version}

Summary:	K Desktop Environment - international support
Summary(pl.UTF-8):	KDE - wsparcie dla wielu języków
Name:		kde4-l10n
Version:	4.0.0
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-ar-%{version}.tar.bz2
# Source0-md5:	ed2c9eaeca75858171f7e0eb0b6dfaf8
Source1:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-be-%{version}.tar.bz2
# Source1-md5:	17d1c63477c00794d9cb2f7145067b27
Source2:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-bg-%{version}.tar.bz2
# Source2-md5:	639694013b12b1c5c6686249caca35b2
Source3:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-ca-%{version}.tar.bz2
# Source3-md5:	84c188799a1f6b62f132d86d0a26d4af
Source4:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-csb-%{version}.tar.bz2
# Source4-md5:	627e0f6f2b740b469ccc0386347c2401
Source5:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-de-%{version}.tar.bz2
# Source5-md5:	9b993472cc3a95c08096c7b4cf44ccbd
Source6:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-el-%{version}.tar.bz2
# Source6-md5:	84f4b2dc719cf31b23e12d38e4a58e91
Source7:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-en_GB-%{version}.tar.bz2
# Source7-md5:	33e271191cd6fe111ac0f0086bdcc2df
Source8:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-eo-%{version}.tar.bz2
# Source8-md5:	c3a70321dfad4d7cf26b571d7ac4992b
Source9:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-es-%{version}.tar.bz2
# Source9-md5:	025f495ca73862f6252c5f11485f111c
Source10:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-et-%{version}.tar.bz2
# Source10-md5:	18b9fdd4932c0c6616485853e5457e22
Source11:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-eu-%{version}.tar.bz2
# Source11-md5:	d39bf627b274093bf6ec9bde5df78323
Source12:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-fi-%{version}.tar.bz2
# Source12-md5:	2289f5841b7dce7656d8236c53f36201
Source13:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-fr-%{version}.tar.bz2
# Source13-md5:	8bf032758a8d94f0246862b215abc70c
Source14:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-ga-%{version}.tar.bz2
# Source14-md5:	a04f5593bbc80dfe594e2cb467a53f31
Source15:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-gl-%{version}.tar.bz2
# Source15-md5:	f038a47bd2e68d2d18b84188f71f030c
Source16:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-hi-%{version}.tar.bz2
# Source16-md5:	72d021ff4fd8e4024b20873e02d4eabc
Source17:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-hu-%{version}.tar.bz2
# Source17-md5:	4f2a2a5d2aff5dfe52e675cbd72b96ce
Source18:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-it-%{version}.tar.bz2
# Source18-md5:	58740ba8ebd39bc923d3a35132432a68
Source19:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-ja-%{version}.tar.bz2
# Source19-md5:	e0293579dc268c4144b01b2ec74b0af2
Source20:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-km-%{version}.tar.bz2
# Source20-md5:	5b510583cb28f5c831ded2ef40bd96ff
Source21:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-ko-%{version}.tar.bz2
# Source21-md5:	7718576a2befb1f6020a1188c0d59b9c
Source22:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-lv-%{version}.tar.bz2
# Source22-md5:	54484cd9ee67bb2d5d4ac38ef611789a
Source23:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-mk-%{version}.tar.bz2
# Source23-md5:	730d6bf451f763190b79b39e0f6df01d
Source24:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-nb-%{version}.tar.bz2
# Source24-md5:	064adc1d231f10abc896bd93d43fc24b
Source25:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-nds-%{version}.tar.bz2
# Source25-md5:	6bad50e95ded65bb4cbc60dcfe81d57e
Source26:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-ne-%{version}.tar.bz2
# Source26-md5:	48fc5404c9619fc85b1c9cfb35e9a1e4
Source27:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-nl-%{version}.tar.bz2
# Source27-md5:	b57e71059596043e57c52e0695b762cc
Source28:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-nn-%{version}.tar.bz2
# Source28-md5:	98e535c726cda118545cfb5d3c786f0e
Source29:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-pa-%{version}.tar.bz2
# Source29-md5:	ab58183d4f539bc3b888bff1a71492ff
Source30:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-pl-%{version}.tar.bz2
# Source30-md5:	a0b889c00cf95d299720e5f3b4c42500
Source31:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-pt-%{version}.tar.bz2
# Source31-md5:	a8e87f9613e95521065d4ba5c65356e5
Source32:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-pt_BR-%{version}.tar.bz2
# Source32-md5:	6eb426b92d668220bfceb910c0635e06
Source33:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-ru-%{version}.tar.bz2
# Source33-md5:	4552842fc7b6dade6cbfa594c4b1e3d0
Source34:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-se-%{version}.tar.bz2
# Source34-md5:	c41de3e29360d33fa7cde0c2264a55e3
Source35:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-sl-%{version}.tar.bz2
# Source35-md5:	bdcbe5504c557fb1a2adf04403f25a7a
Source36:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-sv-%{version}.tar.bz2
# Source36-md5:	f1f553a5cc6896ced8460b95622c1fdc
Source37:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-th-%{version}.tar.bz2
# Source37-md5:	e75222e7dcbf409336cc84f064eb0ffe
Source38:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-tr-%{version}.tar.bz2
# Source38-md5:	40d5986d38e8e06d60569672548dc1fc
Source39:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-uk-%{version}.tar.bz2
# Source39-md5:	23cc2d4dcb5e4254149aa6d6446c0a15
Source40:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-wa-%{version}.tar.bz2
# Source40-md5:	f7e3bce1e525b636f12f35db39ae0498
Source41:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-zh_CN-%{version}.tar.bz2
# Source41-md5:	0681d57cf706f192457fdcc1c8ab9e1f
Source42:	ftp://ftp.kde.org/pub/kde/stable/4.0.0/src/kde-l10n/kde-l10n-zh_TW-%{version}.tar.bz2
# Source42-md5:	b8ef03bac64f7df7a4c95cb9d43da8e7
#Patch0:		%{name}-fa.patch
#Patch1:		%{name}-locale-names.patch
BuildRequires:	cmake
BuildRequires:	gettext-devel
#BuildRequires:	kdelibs-devel
#BuildRequires:	libxml2-progs >= 2.4.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_py_hardlink	1

%description
K Desktop Environment - international support.

%description -l pl.UTF-8
KDE - wsparcie dla wielu języków.

%package base
Summary:	Empty metapackage to handle obsoletes
Summary(pl.UTF-8):	Pusty metapakiet z obsoletes
Group:		X11/Applications
Obsoletes:	common-filemanagement-i18n
Obsoletes:	kde-decoration-b2-i18n
Obsoletes:	kde-decoration-cde-i18n
Obsoletes:	kde-decoration-common-i18n
Obsoletes:	kde-decoration-glow-i18n
Obsoletes:	kde-decoration-icewm-i18n
Obsoletes:	kde-decoration-kde1-i18n
Obsoletes:	kde-decoration-kstep-i18n
Obsoletes:	kde-decoration-modernsys-i18n
Obsoletes:	kde-decoration-openlook-i18n
Obsoletes:	kde-decoration-plastik-i18n
Obsoletes:	kde-decoration-quartz-i18n
Obsoletes:	kde-decoration-riscos-i18n
Obsoletes:	kde-decoration-system-i18n
Obsoletes:	kde-i18n-kdelibs
Obsoletes:	kde-kgreet-classic-i18n
Obsoletes:	kde-kio-imap4-i18n
Obsoletes:	kde-kio-ldap-i18n
Obsoletes:	kde-kio-newimap4-i18n
Obsoletes:	kde-kio-nntp-i18n
Obsoletes:	kde-kio-pop3-i18n
Obsoletes:	kde-kio-smtp-i18n
Obsoletes:	kde-style-plastik-i18n
Obsoletes:	kdeaccessibility-i18n
Obsoletes:	kdeaccessibility-kmag-i18n
Obsoletes:	kdeaccessibility-kmousetool-i18n
Obsoletes:	kdeaccessibility-kmouth-i18n
Obsoletes:	kdeaddons-ark-i18n
Obsoletes:	kdeaddons-atlantikdesigner-i18n
Obsoletes:	kdeaddons-fsview-i18n
Obsoletes:	kdeaddons-i18n
Obsoletes:	kdeaddons-kaddressbook-i18n
Obsoletes:	kdeaddons-kate-i18n
Obsoletes:	kdeaddons-kicker-i18n
Obsoletes:	kdeaddons-konqueror-i18n
Obsoletes:	kdeaddons-kontact-i18n
Obsoletes:	kdeaddons-ksig-i18n
Obsoletes:	kdeaddons-kvim-i18n
Obsoletes:	kdeaddons-lnkforward-i18n
Obsoletes:	kdeaddons-noatun-i18n
Obsoletes:	kdeadmin-i18n
Obsoletes:	kdeadmin-kcmlilo-i18n
Obsoletes:	kdeadmin-kcmlinuz-i18n
Obsoletes:	kdeadmin-kcron-i18n
Obsoletes:	kdeadmin-kdat-i18n
Obsoletes:	kdeadmin-kpackage-i18n
Obsoletes:	kdeadmin-ksysv-i18n
Obsoletes:	kdeadmin-kuser-i18n
Obsoletes:	kdeartwork-i18n
Obsoletes:	kdeartwork-screensavers-i18n
Obsoletes:	kdebase-common-filemanagement-i18n
Obsoletes:	kdebase-core-i18n
Obsoletes:	kdebase-desktop-i18n
Obsoletes:	kdebase-desktop-libs-i18n
Obsoletes:	kdebase-i18n
Obsoletes:	kdebase-infocenter-i18n
Obsoletes:	kdebase-kappfinder-i18n
Obsoletes:	kdebase-kate-i18n
Obsoletes:	kdebase-kdcop-i18n
Obsoletes:	kdebase-kdeprintfax-i18n
Obsoletes:	kdebase-kdialog-i18n
Obsoletes:	kdebase-kfind-i18n
Obsoletes:	kdebase-kfontinst-i18n
Obsoletes:	kdebase-kicker-i18n
Obsoletes:	kdebase-kicker-libs-i18n
Obsoletes:	kdebase-kjobviewer-i18n
Obsoletes:	kdebase-klipper-i18n
Obsoletes:	kdebase-kmenuedit-i18n
Obsoletes:	kdebase-konsole-i18n
Obsoletes:	kdebase-kpager-i18n
Obsoletes:	kdebase-kpersonalizer-i18n
Obsoletes:	kdebase-ksysguard-i18n
Obsoletes:	kdebase-ksystraycmd-i18n
Obsoletes:	kdebase-kwrite-i18n
Obsoletes:	kdebase-libkonq-i18n
Obsoletes:	kdebase-mailnews-i18n
Obsoletes:	kdebase-screensavers-i18n
Obsoletes:	kdebase-useraccount-i18n
Obsoletes:	kdeedu-flashkard-i18n
Obsoletes:	kdeedu-i18n
Obsoletes:	kdeedu-kalzium-i18n
Obsoletes:	kdeedu-kbruch-i18n
Obsoletes:	kdeedu-keduca-i18n
Obsoletes:	kdeedu-khangman-i18n
Obsoletes:	kdeedu-kig-i18n
Obsoletes:	kdeedu-kiten-i18n
Obsoletes:	kdeedu-klatin-i18n
Obsoletes:	kdeedu-klettres-i18n
Obsoletes:	kdeedu-kmessedwords-i18n
Obsoletes:	kdeedu-kmplot-i18n
Obsoletes:	kdeedu-kpercentage-i18n
Obsoletes:	kdeedu-kstars-i18n
Obsoletes:	kdeedu-ktouch-i18n
Obsoletes:	kdeedu-kturtle-i18n
Obsoletes:	kdeedu-kverbos-i18n
Obsoletes:	kdeedu-kvoctrain-i18n
Obsoletes:	kdeedu-kwordquiz-i18n
Obsoletes:	kdegames-atlantik-i18n
Obsoletes:	kdegames-i18n
Obsoletes:	kdegames-kasteroids-i18n
Obsoletes:	kdegames-katomic-i18n
Obsoletes:	kdegames-kbackgammon-i18n
Obsoletes:	kdegames-kbattleship-i18n
Obsoletes:	kdegames-kblackbox-i18n
Obsoletes:	kdegames-kbounce-i18n
Obsoletes:	kdegames-kenolaba-i18n
Obsoletes:	kdegames-kfouleggs-i18n
Obsoletes:	kdegames-kgoldrunner-i18n
Obsoletes:	kdegames-kjumpingcube-i18n
Obsoletes:	kdegames-klickety-i18n
Obsoletes:	kdegames-klines-i18n
Obsoletes:	kdegames-kmahjongg-i18n
Obsoletes:	kdegames-kmines-i18n
Obsoletes:	kdegames-kolf-i18n
Obsoletes:	kdegames-konquest-i18n
Obsoletes:	kdegames-kpat-i18n
Obsoletes:	kdegames-kpoker-i18n
Obsoletes:	kdegames-kreversi-i18n
Obsoletes:	kdegames-ksame-i18n
Obsoletes:	kdegames-kshisen-i18n
Obsoletes:	kdegames-ksirtet-i18n
Obsoletes:	kdegames-ksmiletris-i18n
Obsoletes:	kdegames-ksnake-i18n
Obsoletes:	kdegames-ksokoban-i18n
Obsoletes:	kdegames-kspaceduel-i18n
Obsoletes:	kdegames-ktron-i18n
Obsoletes:	kdegames-ktuberling-i18n
Obsoletes:	kdegames-kwin4-i18n
Obsoletes:	kdegames-lskat-i18n
Obsoletes:	kdegames-megami-i18n
Obsoletes:	kdegraphics-i18n
Obsoletes:	kdegraphics-kamera-i18n
Obsoletes:	kdegraphics-kcoloredit-i18n
Obsoletes:	kdegraphics-kdvi-i18n
Obsoletes:	kdegraphics-kfax-i18n
Obsoletes:	kdegraphics-kfile-i18n
Obsoletes:	kdegraphics-kgamma-i18n
Obsoletes:	kdegraphics-kghostview-i18n
Obsoletes:	kdegraphics-kiconedit-i18n
Obsoletes:	kdegraphics-kmrml-i18n
Obsoletes:	kdegraphics-kolourpaint-i18n
Obsoletes:	kdegraphics-kooka-i18n
Obsoletes:	kdegraphics-kpaint-i18n
Obsoletes:	kdegraphics-kpdf-i18n
Obsoletes:	kdegraphics-kpovmodeler-i18n
Obsoletes:	kdegraphics-kruler-i18n
Obsoletes:	kdegraphics-ksnapshot-i18n
Obsoletes:	kdegraphics-ksvg-i18n
Obsoletes:	kdegraphics-kuickshow-i18n
Obsoletes:	kdegraphics-kview-i18n
Obsoletes:	kdelibs-i18n
Obsoletes:	kdemultimedia-arts-i18n
Obsoletes:	kdemultimedia-artsbuilder-i18n
Obsoletes:	kdemultimedia-artscontrol-i18n
Obsoletes:	kdemultimedia-audiocd-i18n
Obsoletes:	kdemultimedia-i18n
Obsoletes:	kdemultimedia-juk-i18n
Obsoletes:	kdemultimedia-kaboodle-i18n
Obsoletes:	kdemultimedia-kaudiocreator-i18n
Obsoletes:	kdemultimedia-kfile-i18n
Obsoletes:	kdemultimedia-kmid-i18n
Obsoletes:	kdemultimedia-kmix-i18n
Obsoletes:	kdemultimedia-krec-i18n
Obsoletes:	kdemultimedia-kscd-i18n
Obsoletes:	kdemultimedia-libkcddb-i18n
Obsoletes:	kdemultimedia-noatun-i18n
Obsoletes:	kdenetwork-filesharing-i18n
Obsoletes:	kdenetwork-i18n
Obsoletes:	kdenetwork-kdict-i18n
Obsoletes:	kdenetwork-kget-i18n
Obsoletes:	kdenetwork-kinetd-i18n
Obsoletes:	kdenetwork-knewsticker-i18n
Obsoletes:	kdenetwork-kopete-i18n
Obsoletes:	kdenetwork-kpf-i18n
Obsoletes:	kdenetwork-kppp-i18n
Obsoletes:	kdenetwork-krfb-i18n
Obsoletes:	kdenetwork-ksirc-i18n
Obsoletes:	kdenetwork-ktalkd-i18n
Obsoletes:	kdenetwork-kwifimanager-i18n
Obsoletes:	kdenetwork-lanbrowser-i18n
Obsoletes:	kdenetwork-rss-i18n
Obsoletes:	kdepim-i18n
Obsoletes:	kdepim-i18n
Obsoletes:	kdepim-kaddressbook-i18n
Obsoletes:	kdepim-kandy-i18n
Obsoletes:	kdepim-karm-i18n
Obsoletes:	kdepim-kgantt-i18n
Obsoletes:	kdepim-kmail-i18n
Obsoletes:	kdepim-kmail-libs-i18n
Obsoletes:	kdepim-knode-i18n
Obsoletes:	kdepim-knotes-i18n
Obsoletes:	kdepim-konsolekalendar-i18n
Obsoletes:	kdepim-kontact-i18n
Obsoletes:	kdepim-korganizer-i18n
Obsoletes:	kdepim-korganizer-libs-i18n
Obsoletes:	kdepim-korn-i18n
Obsoletes:	kdepim-kpilot-i18n
Obsoletes:	kdepim-ktnef-i18n
Obsoletes:	kdepim-libkcal-i18n
Obsoletes:	kdepim-libkdenetwork-i18n
Obsoletes:	kdepim-libkdepim-i18n
Obsoletes:	kdepim-libksieve-i18n
Obsoletes:	kdepim-libs-i18n
Obsoletes:	kdesdk-cervisia-i18n
Obsoletes:	kdesdk-i18n
Obsoletes:	kdesdk-kbabel-i18n
Obsoletes:	kdesdk-kbugbuster-i18n
Obsoletes:	kdesdk-kcachegrind-i18n
Obsoletes:	kdesdk-kfile-i18n
Obsoletes:	kdesdk-kfilereplace-i18n
Obsoletes:	kdesdk-kompare-i18n
Obsoletes:	kdesdk-kspy-i18n
Obsoletes:	kdesdk-kstartperf-i18n
Obsoletes:	kdesdk-kuiviewer-i18n
Obsoletes:	kdesdk-libcvsservice-i18n
Obsoletes:	kdesdk-spy-i18n
Obsoletes:	kdesdk-umbrello-i18n
Obsoletes:	kdetoys-amor-i18n
Obsoletes:	kdetoys-fifteen-i18n
Obsoletes:	kdetoys-i18n
Obsoletes:	kdetoys-kmoon-i18n
Obsoletes:	kdetoys-kodo-i18n
Obsoletes:	kdetoys-kteatime-i18n
Obsoletes:	kdetoys-ktux-i18n
Obsoletes:	kdetoys-kweather-i18n
Obsoletes:	kdetoys-kworldclock-i18n
Obsoletes:	kdeutils-ark-i18n
Obsoletes:	kdeutils-i18n
Obsoletes:	kdeutils-kcalc-i18n
Obsoletes:	kdeutils-kcharselect-i18n
Obsoletes:	kdeutils-kdelirc-i18n
Obsoletes:	kdeutils-kdepasswd-i18n
Obsoletes:	kdeutils-kdessh-i18n
Obsoletes:	kdeutils-kdf-i18n
Obsoletes:	kdeutils-kedit-i18n
Obsoletes:	kdeutils-kfloppy-i18n
Obsoletes:	kdeutils-kgpg-i18n
Obsoletes:	kdeutils-khexedit-i18n
Obsoletes:	kdeutils-kjots-i18n
Obsoletes:	kdeutils-klaptopdaemon-i18n
Obsoletes:	kdeutils-kmilo-i18n
Obsoletes:	kdeutils-kregexpeditor-i18n
Obsoletes:	kdeutils-ksim-i18n
Obsoletes:	kdeutils-ktimer-i18n
Obsoletes:	kdeutils-kwalletmanager-i18n
Obsoletes:	kdeutils-userinfo-i18n
Obsoletes:	kdevelop-i18n
Obsoletes:	kdewebdev-kfilereplace-i18n
Obsoletes:	kdewebdev-kimagemapeditor-i18n
Obsoletes:	kdewebdev-klinkstatus-i18n
Obsoletes:	kdewebdev-kommander-i18n
Obsoletes:	kdewebdev-kxsldbg-i18n
Obsoletes:	kdewebdev-quanta-i18n
Obsoletes:	kdm-i18n
Obsoletes:	konqueror-i18n
Obsoletes:	konqueror-libs-i18n
Obsoletes:	quanta-i18n
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7

%description base
Empty metapackage to handle obsoletes for individual i18n subpackages.

%description base -l pl.UTF-8
Pusty metapakiet z Obsoletes dla oddzielnych podpakietów i18n.

%package Afrikaans
Summary:	K Desktop Environment - Afrikaans language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka afrykanerskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
# "Affrikaans" is here intentionally, to allow upgrade from misspelled packages
Obsoletes:	kde-i18n-Affrikaans

%description Afrikaans
K Desktop Environment - Afrikaans language support.

%description Afrikaans -l pl.UTF-8
KDE - wsparcie dla języka afrykanerskiego.

%package Arabic
Summary:	K Desktop Environment - Arabic language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka arabskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Arabic
K Desktop Environment - Arabic language support.

%description Arabic -l pl.UTF-8
KDE - wsparcie dla języka arabskiego.

%package Azerbaijani
Summary:	K Desktop Environment - Azerbaijani language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka azerskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Azerbaijani
K Desktop Environment - Azerbaijani language support.

%description Azerbaijani -l pl.UTF-8
KDE - wsparcie dla języka azerskiego.

%package Bulgarian
Summary:	K Desktop Environment - Bulgarian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka bułgarskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Bulgarian
K Desktop Environment - Bulgarian language support.

%description Bulgarian -l pl.UTF-8
KDE - wsparcie dla języka bułgarskiego.

%package Bengali
Summary:	K Desktop Environment - Bengali language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka bengalskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Bengali
K Desktop Environment - Bengali language support.

%description Bengali -l pl.UTF-8
KDE - wsparcie dla języka bengalskiego.

%package Breton
Summary:	K Desktop Environment - Breton language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka bretońskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Breton
K Desktop Environment - Breton language support.

%description Breton -l pl.UTF-8
KDE - wsparcie dla języka bretońskiego.

%package Bosnian
Summary:	K Desktop Environment - Bosnian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka bośniackiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Bosnian
K Desktop Environment - Bosnian language support.

%description Bosnian -l pl.UTF-8
KDE - wsparcie dla języka bośniackiego.

%package Catalan
Summary:	K Desktop Environment - Catalan language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka katalońskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Catalan
K Desktop Environment - Catalan language support.

%description Catalan -l pl.UTF-8
KDE - wsparcie dla języka katalońskiego.

%package Czech
Summary:	K Desktop Environment - Czech language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka czeskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Czech
K Desktop Environment - Czech language support.

%description Czech -l pl.UTF-8
KDE - wsparcie dla języka czeskiego.

%package Kashubian
Summary:	K Desktop Environment - Kashubian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka kaszubskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Kashubian
K Desktop Environment - Kashubian language support.

%description Kashubian -l pl.UTF-u
KDE - wsparcie dla języka kaszubskiego.

%package Cymraeg
Summary:	K Desktop Environment - Cymraeg language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka walijskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Cymraeg
K Desktop Environment - Cymraeg language support.

%description Cymraeg -l pl.UTF-8
KDE - wsparcie dla języka walijskiego.

%package Danish
Summary:	K Desktop Environment - Danish language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka duńskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Danish
K Desktop Environment - Danish language support.

%description Danish -l pl.UTF-8
KDE - wsparcie dla języka duńskiego.

%package German
Summary:	K Desktop Environment - German language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka niemieckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description German
K Desktop Environment - German language support.

%description German -l pl.UTF-8
KDE - wsparcie dla języka niemieckiego.

%package Greek
Summary:	K Desktop Environment - Greek language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka greckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Greek
K Desktop Environment - Greek language support.

%description Greek -l pl.UTF-8
KDE - wsparcie dla języka greckiego.

%package English
Summary:	K Desktop Environment - English language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka angielskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description English
K Desktop Environment - English language support.

%description English -l pl.UTF-8
KDE - wsparcie dla języka angielskiego.

%package English_UK
Summary:	K Desktop Environment - K Desktop Environment - English (UK) language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka angielskiego (odmiany brytyjskiej)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description English_UK
K Desktop Environment - English (UK) language support.

%description English_UK -l pl.UTF-8
KDE - wsparcie dla języka angielskiego (odmiany brytyjskiej).

%package Esperanto
Summary:	K Desktop Environment - Esperanto language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka esperanto
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Esperanto
K Desktop Environment - Esperanto language support.

%description Esperanto -l pl.UTF-8
KDE - wsparcie dla języka esperanto.

%package Spanish
Summary:	K Desktop Environment - Spanish language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka hiszpańskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Spanish
K Desktop Environment - Spanish language support.

%description Spanish -l pl.UTF-8
KDE - wsparcie dla języka hiszpańskiego.

%package Estonian
Summary:	K Desktop Environment - Estonian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka estońskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Estonian
K Desktop Environment - Estonian language support.

%description Estonian -l pl.UTF-8
KDE - wsparcie dla języka estońskiego.

%package Basque
Summary:	K Desktop Environment - Basque language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka baskijskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Basque
K Desktop Environment - Basque language support.

%description Basque -l pl.UTF-8
KDE - wsparcie dla języka baskijskiego.

%package Farsi
Summary:	K Desktop Environment - Farsi language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka perskiego (farsi)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Farsi
K Desktop Environment - Farsi language support.

%description Farsi -l pl.UTF-8
KDE - wsparcie dla języka perskiego (farsi).

%package Finnish
Summary:	K Desktop Environment - Finnish language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka fińskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Finnish
K Desktop Environment - Finnish language support.

%description Finnish -l pl.UTF-8
KDE - wsparcie dla języka fińskiego.

%package French
Summary:	K Desktop Environment - French language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka francuskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description French
K Desktop Environment - French language support.

%description French -l pl.UTF-8
KDE - wsparcie dla języka francuskiego.

%package Frisian
Summary:	K Desktop Environment - Frisian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka fryzyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Frisian
K Desktop Environment - Frisian language support.

%description Frisian -l pl.UTF-8
KDE - wsparcie dla języka fryzyjskiego.

%package Irish
Summary:	K Desktop Environment - Irish language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka irlandzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Irish
K Desktop Environment - Irish language support.

%description Irish -l pl.UTF-8
KDE - wsparcie dla języka irlandzkiego.

%package Galician
Summary:	K Desktop Environment - Galician language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka galicyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Galician
K Desktop Environment - Galician language support.

%description Galician -l pl.UTF-8
KDE - wsparcie dla języka galicyjskiego.

%package Hindi
Summary:	K Desktop Environment - Hindi language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka hindi
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Hindi
K Desktop Environment - Hindi language support.

%description Hindi -l pl.UTF-8
KDE - wsparcie dla języka hindi.

%package Hebrew
Summary:	K Desktop Environment - Hebrew language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka hebrajskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Hebrew
K Desktop Environment - Hebrew language support.

%description Hebrew -l pl.UTF-8
KDE - wsparcie dla języka hebrajskiego.

%package Croatian
Summary:	K Desktop Environment - Croatian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka chorwackiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Croatian
K Desktop Environment - Croatian language support.

%description Croatian -l pl.UTF-8
KDE - wsparcie dla języka chorwackiego.

%package Upper_Sorbian
Summary:	K Desktop Environment - Upper Sorbian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka górnołużyckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Upper_Sorbian
K Desktop Environment - Upper Sorbian language support.

%description Upper_Sorbian  -l pl.UTF-8
KDE - wsparcie dla języka górnołużyckiego.

%package Hungarian
Summary:	K Desktop Environment - Hungarian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka węgierskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Hungarian
K Desktop Environment - Hungarian language support.

%description Hungarian -l pl.UTF-8
KDE - wsparcie dla języka węgierskiego.

%package Indonesian
Summary:	K Desktop Environment - Indonesian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka indonezyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Indonesian
K Desktop Environment - Indonesian language support.

%description Indonesian -l pl.UTF-8
KDE - wsparcie dla języka indonezyjskiego.

%package Icelandic
Summary:	K Desktop Environment - Icelandic language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka islandzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Icelandic
K Desktop Environment - Icelandic language support.

%description Icelandic -l pl.UTF-8
KDE - wsparcie dla języka islandzkiego.

%package Italian
Summary:	K Desktop Environment - Italian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka włoskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Italian
K Desktop Environment - Italian language support.

%description Italian -l pl.UTF-8
KDE - wsparcie dla języka włoskiego.

%package Japanese
Summary:	K Desktop Environment - Japanese language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka japońskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Japanese
K Desktop Environment - Japanese language support.

%description Japanese -l pl.UTF-8
KDE - wsparcie dla języka japońskiego.

%package Kazakh
Summary:	K Desktop Environment - Kazakh language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka kazaskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Kazakh
K Desktop Environment - Kazakh language support.

%description Kazakh -l pl.UTF-8
KDE - wsparcie dla języka kazaskiego.

%package Khmer
Summary:	K Desktop Environment - Khmer language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka khmerskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Khmer
K Desktop Environment - Khmer language support.

%description Khmer -l pl.UTF-8
KDE - wsparcie dla języka khmerskiego.

%package Kinyarwanda
Summary:	K Desktop Environment - Kinyarwanda language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka kinya-ruanda
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Kinyarwanda
K Desktop Environment - Kinyarwanda language support.

%description Kinyarwanda -l pl.UTF-8
KDE - wsparcie dla języka kinya-ruanda.

%package Korean
Summary:	K Desktop Environment - Korean language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka koreańskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Korean
K Desktop Environment - Korean language support.

%description Korean -l pl.UTF-8
KDE - wsparcie dla języka koreańskiego.

%package Lithuanian
Summary:	K Desktop Environment - Lithuanian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka litewskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Lithuanian
K Desktop Environment - Lithuanian language support.

%description Lithuanian -l pl.UTF-8
KDE - Wsparcie dla języka litewskiego.

%package Lao
Summary:	K Desktop Environment - Lao language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka laotańskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Lao
K Desktop Environment - lao language support.

%description Lao -l pl.UTF-8
KDE - wsparcie dla języka laotańskiego.

%package Latvian
Summary:	K Desktop Environment - Latvian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka łotewskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Latvian
K Desktop Environment - Latvian language support.

%description Latvian -l pl.UTF-8
KDE - wsparcie dla języka łotewskiego.

%package Maori
Summary:	K Desktop Environment - Maori language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka maoryjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Maori
K Desktop Environment - Maori language support.

%description Maori -l pl.UTF-8
KDE - wsparcie dla języka maoryjskiego.

%package Macedonian
Summary:	K Desktop Environment - Macedonian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka macedońskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Macedonian
K Desktop Environment - Macedonian language support.

%description Macedonian -l pl.UTF-8
KDE - wsparcie dla języka macedońskiego.

%package Malay
Summary:	K Desktop Environment - Malay language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka malajskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Malay
K Desktop Environment - Malay language support.

%description Malay -l pl.UTF-8
KDE - wsparcie dla języka malajskiego.

%package Maltese
Summary:	K Desktop Environment - Maltese language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka maltańskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Maltese
K Desktop Environment - Maltese language support.

%description Maltese -l pl.UTF-8
KDE - wsparcie dla języka maltańskiego.

%package Mongolian
Summary:	K Desktop Environment - Mongolian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka mongolskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Mongolian
K Desktop Environment - Mongolian language support.

%description Mongolian -l pl.UTF-8
KDE - wsparcie dla języka mongolskiego.

%package Low_Saxon
Summary:	K Desktop Environment - Low Saxon language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka dolnosaksońskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Low_Saxon
K Desktop Environment - Low Saxon language support.

%description Low_Saxon -l pl.UTF-8
KDE - wsparcie dla języka dolnosaksońskiego.

%package Dutch
Summary:	K Desktop Environment - Dutch language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka holenderskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Dutch
K Desktop Environment - Dutch language support.

%description Dutch -l pl.UTF-8
KDE - wsparcie dla języka holenderskiego.

%package Norwegian_Bokmaal
Summary:	K Desktop Environment - Norwegian (Bokmaal) language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka norweskiego (odmiany bokmaal)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
# "Bookmal" is here intentionally, to allow upgrade from misspelled packages
Obsoletes:	kde-i18n-Norwegian_Bookmal

%description Norwegian_Bokmaal
K Desktop Environment - Norwegian (Bokmaal) language support.

%description Norwegian_Bokmaal -l pl.UTF-8
KDE - wsparcie dla języka norweskiego (odmiany bokmaal).

%package Norwegian_Nynorsk
Summary:	K Desktop Environment - Norwegian (Nynorsk) language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka norweskiego (odmiany nynorsk)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Norwegian_Nynorsk
K Desktop Environment - Norwegian (Nynorsk) language support.

%description Norwegian_Nynorsk -l pl.UTF-8
KDE - wsparcie dla języka norweskiego (odmiany nynorsk).

%package Northern_Sotho
Summary:	K Desktop Environment - Northern Sotho language support
Summary(pl.UTF-8):	KDE - wsparcie dla północnej odmiany języka ludu Soto
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Northern_Sotho
K Desktop Environment - Northern Sotho language support.

%description Northern_Sotho -l pl.UTF-8
KDE - wsparcie dla północnej odmiany języka ludu Soto.

%package Gascon_Occitan
Summary:	K Desktop Environment - Occitan (Gascon) language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka oksytańskiego (dialektu gaskońskiego)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	kde-i18n-Gascon_occitan

%description Gascon_Occitan
K Desktop Environment - Occitan (Gascon) language support.

%description Gascon_Occitan -l pl.UTF-8
KDE - wsparcie dla języka oksytańskiego (dialektu gaskońskiego).

%package Punjabi
Summary:	K Desktop Environment - Punjabi language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka pendżabskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Punjabi
K Desktop Environment - Punjabi language support.

%description Punjabi -l pl.UTF-8
KDE - wsparcie dla języka pendżabskiego.

%package Polish
Summary:	K Desktop Environment - Polish language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka polskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Polish
K Desktop Environment - Polish language support.

%description Polish -l pl.UTF-8
KDE - wsparcie dla języka polskiego.

%package Portuguese
Summary:	K Desktop Environment - Portuguese language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka portugalskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
# "Portugnese" is here intentionally, to allow upgrade from misspelled packages
Obsoletes:	kde-i18n-Portugnese

%description Portuguese
K Desktop Environment - Portuguese language support.

%description Portuguese -l pl.UTF-8
KDE - wsparcie dla języka portugalskiego.

%package Brazil_Portuguese
Summary:	K Desktop Environment - Portuguese (Brazil) language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka portugalskiego (odmiany brazylijskiej)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}
# "Brazil_Protugnese" is here intentionally, to allow upgrade from misspelled packages
Obsoletes:	kde-i18n-Brazil_Protugnese

%description Brazil_Portuguese
K Desktop Environment - Portuguese (Brazil) language support.

%description Brazil_Portuguese -l pl.UTF-8
KDE - wsparcie dla języka portugalskiego (odmiany brazylijskiej).

%package Romanian
Summary:	K Desktop Environment - Romanian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka rumuńskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Romanian
K Desktop Environment - Romanian language support.

%description Romanian -l pl.UTF-8
KDE - wsparcie dla języka rumuńskiego.

%package Russian
Summary:	K Desktop Environment - Russian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka rosyjskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Russian
K Desktop Environment - Russian language support.

%description Russian -l pl.UTF-8
KDE - wsparcie dla języka rosyjskiego.

%package Swati
Summary:	K Desktop Environment - Swati language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka swati
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Swati
K Desktop Environment - Swati language support.

%description Swati -l pl.UTF-8
KDE - wsparcie dla języka swati.

%package Northern_Sami
Summary:	K Desktop Environment - Northern Sami language support
Summary(pl.UTF-8):	KDE - wsparcie dla północnego języka saami (lapońskiego)
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Northern_Sami
K Desktop Environment - Northern Sami language support.

%description Northern_Sami -l pl.UTF-8
KDE - wsparcie dla północnego języka saami (lapońskiego).

%package Slovak
Summary:	K Desktop Environment - Slovak language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka słowackiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Slovak
K Desktop Environment - Slovak language support.

%description Slovak -l pl.UTF-8
KDE - wsparcie dla języka słowackiego.

%package Slovenian
Summary:	K Desktop Environment - Slovenian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka słoweńskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Slovenian
K Desktop Environment - Slovenian language support.

%description Slovenian -l pl.UTF-8
KDE - wsparcie dla języka słoweńskiego.

%package Serbian
Summary:	K Desktop Environment - Serbian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka serbskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Serbian
K Desktop Environment - Serbian language support.

%description Serbian -l pl.UTF-8
KDE - wsparcie dla języka serbskiego.

%package Swedish
Summary:	K Desktop Environment - Swedish language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka szwedzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Swedish
K Desktop Environment - Swedish language support.

%description Swedish -l pl.UTF-8
KDE - wsparcie dla języka szwedzkiego.

%package Tajik
Summary:	K Desktop Environment - Tajik language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka tadżyckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Tajik
K Desktop Environment - Tajik language support.

%description Tajik -l pl.UTF-8
KDE - wsparcie dla języka tadżyckiego.

%package Tamil
Summary:	K Desktop Environment - Tamil language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka tamilskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Tamil
K Desktop Environment - Tamil language support.

%description Tamil -l pl.UTF-8
KDE - wsparcie dla języka tamilskiego.

%package Telugu
Summary:	K Desktop Environment - Telugu language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka telugu
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Telugu
K Desktop Environment - Telugu language support.

%description Telugu -l pl.UTF-8
KDE - wsparcie dla języka telugu.

%package Thai
Summary:	K Desktop Environment - Thai language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka tajlandzkiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Thai
K Desktop Environment - Thai language support.

%description Thai -l pl.UTF-8
KDE - wsparcie dla języka tajlandzkiego.

%package Turkish
Summary:	K Desktop Environment - Turkish language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka tureckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Turkish
K Desktop Environment - Turkish language support.

%description Turkish -l pl.UTF-8
KDE - wsparcie dla języka tureckiego.

%package Ukrainian
Summary:	K Desktop Environment - Ukrainian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka ukraińskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Ukrainian
K Desktop Environment - Ukrainian language support.

%description Ukrainian -l pl.UTF-8
KDE - wsparcie dla języka ukraińskiego.

%package Uzbek
Summary:	K Desktop Environment - Uzbek language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka uzbeckiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Uzbek
K Desktop Environment - Uzbek language support.

%description Uzbek -l pl.UTF-8
KDE - wsparcie dla języka uzbeckiego.

%package Venda
Summary:	K Desktop Environment - Venda language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka venda
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Venda
K Desktop Environment - Venda language support.

%description Venda -l pl.UTF-8
KDE - wsparcie dla języka venda.

%package Vietnamese
Summary:	K Desktop Environment - Vietnamese language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka wietnamskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Vietnamese
K Desktop Environment - Vietnamese language support.

%description Vietnamese -l pl.UTF-8
KDE - wsparcie dla języka wietnamskiego.

%package Walloon
Summary:	K Desktop Environment - Walloon language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka walońskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Walloon
K Desktop Environment - Walloon language support.

%description Walloon -l pl.UTF-8
KDE - wsparcie dla języka walońskiego.

%package Xhosa
Summary:	K Desktop Environment - Xhosa language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka khosa
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Xhosa
K Desktop Environment - Xhosa language support.

%description Xhosa -l pl.UTF-8
KDE - wsparcie dla języka khosa.

%package Simplified_Chinese
Summary:	K Desktop Environment - simplified Chinese language support
Summary(pl.UTF-8):	KDE - wsparcie dla uproszczonego języka chińskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Simplified_Chinese
K Desktop Environment - simplified Chinese language support.

%description Simplified_Chinese -l pl.UTF-8
KDE - wsparcie dla uproszczonego języka chińskiego.

%package Chinese
Summary:	K Desktop Environment - Chinese language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka chińskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Chinese
K Desktop Environment - Chinese language support.

%description Chinese -l pl.UTF-8
KDE - wsparcie dla języka chińskiego.

%package Zulu
Summary:	K Desktop Environment - Zulu language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka zuluskiego
Group:		X11/Applications
Requires:	%{name}-base = %{version}-%{release}

%description Zulu
K Desktop Environment - Zulu language support.

%description Zulu -l pl.UTF-8
KDE - wsparcie dla języka zuluskiego.

%prep
%setup -qcT %(seq -f '-a %g' 0 42 | xargs)
#%patch0 -p1
#%patch1 -p1

%build
for dir in kde-l10n-*-%{version}; do
	cd $dir
	%cmake \
		-DCMAKE_INSTALL_PREFIX=%{_prefix} \
		-DCMAKE_VERBOSE_MAKEFILE=1 \
		-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
		.
	%{__make}
	cd ..
done

%install
if [ ! -f makeinstall.stamp -o ! -d $RPM_BUILD_ROOT ]; then
	rm -rf makeinstall.stamp installed.stamp $RPM_BUILD_ROOT

	for dir in kde-l10n-*-%{version}; do
		%{__make} -C "$dir" install \
			DESTDIR=$RPM_BUILD_ROOT \
			kde_htmldir="%{_kdedocdir}" \
			kde_libs_htmldir="%{_kdedocdir}"
	done
	touch makeinstall.stamp
fi

if [ ! -f installed.stamp ]; then
	# remove empty language catalogs (= 1 message only)
	find $RPM_BUILD_ROOT%{_datadir}/locale -type f -name '*.mo' | xargs file | egrep ', 1 messages$' | cut -d: -f1 | xargs rm -vf

	# TODO: verify is this renaming ok
	mv $RPM_BUILD_ROOT%{_datadir}/apps/katepart/syntax/logohighlightstyle.de{_DE,}.xml
	mv $RPM_BUILD_ROOT%{_datadir}/apps/katepart/syntax/logohighlightstyle.fr{_FR,}.xml
	mv $RPM_BUILD_ROOT%{_datadir}/apps/kturtle/data/logokeywords.de{_DE,}.xml
	mv $RPM_BUILD_ROOT%{_datadir}/apps/kturtle/data/logokeywords.fr{_FR,}.xml
	mv $RPM_BUILD_ROOT%{_datadir}/apps/kturtle/examples/de{_DE,}
	mv $RPM_BUILD_ROOT%{_datadir}/apps/kturtle/examples/fr{_FR,}

	# useless for the user
	rm $RPM_BUILD_ROOT%{_datadir}/locale/nb/README
	rm $RPM_BUILD_ROOT%{_datadir}/locale/se/ChangeLog
	rm $RPM_BUILD_ROOT%{_datadir}/locale/fr/nbsp_gui_fr.txt
	rm $RPM_BUILD_ROOT%{_datadir}/locale/fr/relecture_docs
	rm $RPM_BUILD_ROOT%{_datadir}/locale/fr/relecture_gui
	rm $RPM_BUILD_ROOT%{_datadir}/locale/da/da.compendium

	# junk
	rm $RPM_BUILD_ROOT%{_datadir}/locale/mn/30x16.png
	rm $RPM_BUILD_ROOT%{_datadir}/locale/mn/60x40.png
	rm $RPM_BUILD_ROOT%{_datadir}/locale/fa/COPYING

	touch installed.stamp
fi

FindLang() {
	# $1 - short language name
	local lang="$1"

	echo "%defattr(644,root,root,755)"

	# share/doc/kde/HTML/(%%lang)
	if [ -d "$RPM_BUILD_ROOT%{_kdedocdir}/$lang" ]; then
		echo "%lang($lang) %{_kdedocdir}/$lang"
	fi

	# share/locale/(%%lang)
	if [ -d "$RPM_BUILD_ROOT%{_datadir}/locale/$lang" ]; then
		echo "%lang($lang) %{_datadir}/locale/$lang/[cef]*"
		echo "%lang($lang) %{_datadir}/locale/$lang/LC_MESSAGES/*.mo"
	fi

	# share/apps/amor/tips-(%%lang)
	if [ -f "$RPM_BUILD_ROOT%{_datadir}/apps/amor/tips-$lang" ]; then
		echo "%lang($lang) %{_datadir}/apps/amor/tips-$lang"
	fi

	# share/apps/katepart/syntax/logohighlightstyle.(%%lang).xml
	if [ -f "$RPM_BUILD_ROOT%{_datadir}/apps/katepart/syntax/logohighlightstyle.$lang.xml" ]; then
		echo "%lang($lang) %{_datadir}/apps/katepart/syntax/logohighlightstyle.$lang.xml"
	fi

	# share/apps/ktuberling/sounds/(%%lang)
	if [ -d "$RPM_BUILD_ROOT%{_datadir}/apps/ktuberling/sounds/$lang" ]; then
		echo "%lang($lang) %{_datadir}/apps/ktuberling/sounds/$lang"
	fi

	# share/apps/khangman/(%lang).txt
	if [ -f "$RPM_BUILD_ROOT%{_datadir}/apps/khangman/$lang.txt" ]; then
		echo "%lang($lang) %{_datadir}/apps/khangman/$lang.txt"
	fi

	# share/apps/khangman/data/(%lang)
	if [ -d "$RPM_BUILD_ROOT%{_datadir}/apps/khangman/data/$lang" ]; then
		echo "%lang($lang) %{_datadir}/apps/khangman/data/$lang"
	fi

	# share/apps/klatin/data/vocabs/(%lang)
	if [ -d "$RPM_BUILD_ROOT%{_datadir}/apps/klatin/data/vocabs/$lang" ]; then
		echo "%lang($lang) %{_datadir}/apps/klatin/data/vocabs/$lang"
	fi

	# share/apps/klettres/(%lang)
	if [ -d "$RPM_BUILD_ROOT%{_datadir}/apps/klettres/$lang" ]; then
		echo "%lang($lang) %{_datadir}/apps/klettres/$lang"
	fi

	# share/apps/kturtle/data/logokeywords.(%lang).xml
	if [ -f "$RPM_BUILD_ROOT%{_datadir}/apps/kturtle/data/logokeywords.$lang.xml" ]; then
		echo "%lang($lang) %{_datadir}/apps/kturtle/data/logokeywords.$lang.xml"
	fi

	# share/apps/kturtle/examples/(%lang)
	if [ -d "$RPM_BUILD_ROOT%{_datadir}/apps/kturtle/examples/$lang" ]; then
		echo "%lang($lang) %{_datadir}/apps/kturtle/examples/$lang"
	fi

	# share/apps/kanagram/data/et/elukutsed.kvtml
	if [ -d "$RPM_BUILD_ROOT%{_datadir}/apps/kanagram/data/$lang" ]; then
		echo "%lang($lang) %{_datadir}/apps/kanagram/data/$lang"
	fi

	touch $lang.ok
}

%if 0
# make symlinks relative
for lang in $RPM_BUILD_ROOT%{_kdedocdir}/*; do
	[ -d $lang ] || continue

	if [ ! -d $lang/common ]; then
		ln -s ../en/common $lang/common
	fi

	for i in $lang/*/*/*; do
		if [ -d $i -a -L $i/common ]; then
			rm -f $i/common
			ln -sf ../../../common $i
		fi
	done

	for i in $lang/*/*; do
		if [ -d $i -a -L $i/common ]; then
			rm -f $i/common
			ln -sf ../../common $i
		fi
	done

	for i in $lang/*; do
		if [ -d $i -a -L $i/common ]; then
			rm -f $i/common
			ln -sf ../common $i
		fi
	done
done
%endif

rm -f *.lang *.cache __find.* *.ok

FindLang af > Afrikaans.lang
FindLang ar > Arabic.lang
FindLang az > Azerbaijani.lang
FindLang bg > Bulgarian.lang
FindLang bn > Bengali.lang
FindLang br > Breton.lang
FindLang bs > Bosnian.lang
FindLang ca > Catalan.lang
FindLang cs > Czech.lang
FindLang csb > Kashubian.lang
FindLang cy > Cymraeg.lang
FindLang da > Danish.lang
FindLang de > German.lang
FindLang el > Greek.lang
#FindLang en > English.lang
FindLang en_GB > English_UK.lang
FindLang eo > Esperanto.lang
FindLang es > Spanish.lang
FindLang et > Estonian.lang
FindLang eu > Basque.lang
FindLang fa > Farsi.lang
FindLang fi > Finnish.lang
FindLang fr > French.lang
FindLang fy > Frisian.lang
FindLang ga > Irish.lang
FindLang gl > Galician.lang
FindLang he > Hebrew.lang
FindLang hi > Hindi.lang
FindLang hr > Croatian.lang
#FindLang hsb > Upper_Sorbian.lang
FindLang hu > Hungarian.lang
#FindLang id > Indonesian.lang
FindLang is > Icelandic.lang
FindLang it > Italian.lang
FindLang ja > Japanese.lang
FindLang kk > Kazakh.lang
FindLang km > Khmer.lang
FindLang ko > Korean.lang
FindLang lt > Lithuanian.lang
FindLang lv > Latvian.lang
#FindLang mi > Maori.lang
FindLang mk > Macedonian.lang
FindLang mn > Mongolian.lang
FindLang ms > Malay.lang
#FindLang mt > Maltese.lang
FindLang nb > Norwegian_Bokmaal.lang
FindLang nds > Low_Saxon.lang
FindLang nl > Dutch.lang
FindLang nn > Norwegian_Nynorsk.lang
FindLang pa > Punjabi.lang
#FindLang nso > Northern_Sotho.lang
#FindLang oc > Gascon_Occitan.lang
FindLang pl > Polish.lang
FindLang pt > Portuguese.lang
FindLang pt_BR > Brazil_Portuguese.lang
FindLang ro > Romanian.lang
FindLang rw > Kinyarwanda.lang
FindLang ru > Russian.lang
FindLang ss > Swati.lang
FindLang se > Northern_Sami.lang
FindLang sk > Slovak.lang
FindLang sl > Slovenian.lang
FindLang sr > Serbian.lang
FindLang sr@latin >> Serbian.lang
FindLang sv > Swedish.lang
FindLang ta > Tamil.lang
FindLang te > Telugu.lang
FindLang tg > Tajik.lang
FindLang th > Thai.lang
FindLang tr > Turkish.lang
FindLang uk > Ukrainian.lang
FindLang uz > Uzbek.lang
#FindLang ven > Venda.lang
FindLang vi > Vietnamese.lang
FindLang wa > Walloon.lang
#FindLang xh > Xhosa.lang
FindLang zh_CN > Simplified_Chinese.lang
FindLang zh_TW > Chinese.lang
#FindLang zu > Zulu.lang

check_installed_languages() {
	err=0
	# we ignore dialects (currently sr@latin is the only case)
	for a in $(ls -1d %{name}-*-%{version} | %{__sed} '/@/d'); do
		l=${a#%{name}-}
		l=${l%%-%{version}}
		if [ ! -f $l.ok ]; then
			echo >&2 "language $l not processed"
			err=1
		fi
	done
	if [ "$err" = 1 ]; then
		exit 1
	fi
}
check_installed_languages

%clean
check_installed_files() {
	err=0
	for a in *.lang; do
		lang=${a%%.lang}

		rpmfile=%{_rpmdir}/%{name}-$lang-%{version}-%{release}.%{_target_cpu}.rpm
		if [ ! -f $rpmfile ]; then
			echo >&2 "Missing %%files section for $lang"
			err=1
		fi
	done
	if [ "$err" = 1 ]; then
		exit 1
	fi
}
check_installed_files
%{!?debug:rm -rf $RPM_BUILD_ROOT}

%files base
%defattr(644,root,root,755)

%files -f Afrikaans.lang Afrikaans
%defattr(644,root,root,755)

%files -f Arabic.lang Arabic
%defattr(644,root,root,755)

%files -f Azerbaijani.lang Azerbaijani
%defattr(644,root,root,755)

%files -f Bulgarian.lang Bulgarian
%defattr(644,root,root,755)

%files -f Bengali.lang Bengali
%defattr(644,root,root,755)

%files -f Breton.lang Breton
%defattr(644,root,root,755)

%files -f Bosnian.lang Bosnian
%defattr(644,root,root,755)

%files -f Catalan.lang Catalan
%defattr(644,root,root,755)

%files -f Czech.lang Czech
%defattr(644,root,root,755)

%files -f Cymraeg.lang Cymraeg
%defattr(644,root,root,755)

%files -f Danish.lang Danish
%defattr(644,root,root,755)

%files -f German.lang German
%defattr(644,root,root,755)

%files -f Greek.lang Greek
%defattr(644,root,root,755)

# %files -f English.lang English

%files -f English_UK.lang English_UK
%defattr(644,root,root,755)

%files -f Esperanto.lang Esperanto
%defattr(644,root,root,755)

%files -f Spanish.lang Spanish
%defattr(644,root,root,755)

%files -f Estonian.lang Estonian
%defattr(644,root,root,755)

%files -f Basque.lang Basque
%defattr(644,root,root,755)

%files -f Farsi.lang Farsi
%defattr(644,root,root,755)

%files -f Finnish.lang Finnish
%defattr(644,root,root,755)

%files -f French.lang French
%defattr(644,root,root,755)

%files -f Frisian.lang Frisian
%defattr(644,root,root,755)

%files -f Irish.lang Irish
%defattr(644,root,root,755)

%files -f Galician.lang Galician
%defattr(644,root,root,755)

%files -f Hindi.lang Hindi
%defattr(644,root,root,755)

%files -f Hebrew.lang Hebrew
%defattr(644,root,root,755)

%files -f Croatian.lang Croatian
%defattr(644,root,root,755)

#%files -f Upper_Sorbian.lang Upper_Sorbian
#%defattr(644,root,root,755)

%files -f Hungarian.lang Hungarian
%defattr(644,root,root,755)

#%files -f Indonesian.lang Indonesian

%files -f Icelandic.lang Icelandic
%defattr(644,root,root,755)

%files -f Italian.lang Italian
%defattr(644,root,root,755)

%files -f Japanese.lang Japanese
%defattr(644,root,root,755)

%files -f Kazakh.lang Kazakh
%defattr(644,root,root,755)

%files -f Khmer.lang Khmer
%defattr(644,root,root,755)

%files -f Korean.lang Korean
%defattr(644,root,root,755)

%files -f Kashubian.lang Kashubian
%defattr(644,root,root,755)

%files -f Lithuanian.lang Lithuanian
%defattr(644,root,root,755)

%files -f Kinyarwanda.lang Kinyarwanda
%defattr(644,root,root,755)

%files -f Latvian.lang Latvian
%defattr(644,root,root,755)

#%files -f Maltese.lang Maltese

%files -f Malay.lang Malay
%defattr(644,root,root,755)

%files -f Mongolian.lang Mongolian
%defattr(644,root,root,755)

#%files -f Maori.lang Maori

%files -f Macedonian.lang Macedonian
%defattr(644,root,root,755)

%files -f Low_Saxon.lang Low_Saxon
%defattr(644,root,root,755)

%files -f Dutch.lang Dutch
%defattr(644,root,root,755)

%files -f Norwegian_Bokmaal.lang Norwegian_Bokmaal
%defattr(644,root,root,755)

%files -f Norwegian_Nynorsk.lang Norwegian_Nynorsk
%defattr(644,root,root,755)

#%files -f Northern_Sotho.lang Northern_Sotho

#%files -f Gascon_Occitan.lang Gascon_Occitan

%files -f Punjabi.lang Punjabi
%defattr(644,root,root,755)

%files -f Polish.lang Polish
%defattr(644,root,root,755)

%files -f Portuguese.lang Portuguese
%defattr(644,root,root,755)

%files -f Brazil_Portuguese.lang Brazil_Portuguese
%defattr(644,root,root,755)

%files -f Romanian.lang Romanian
%defattr(644,root,root,755)

%files -f Russian.lang Russian
%defattr(644,root,root,755)

%files -f Northern_Sami.lang Northern_Sami
%defattr(644,root,root,755)

%files -f Swati.lang Swati
%defattr(644,root,root,755)

%files -f Slovak.lang Slovak
%defattr(644,root,root,755)

%files -f Slovenian.lang Slovenian
%defattr(644,root,root,755)

%files -f Serbian.lang Serbian
%defattr(644,root,root,755)

%files -f Swedish.lang Swedish
%defattr(644,root,root,755)

%files -f Tamil.lang Tamil
%defattr(644,root,root,755)

%files -f Telugu.lang Telugu
%defattr(644,root,root,755)

%files -f Thai.lang Thai
%defattr(644,root,root,755)

%files -f Turkish.lang Turkish
%defattr(644,root,root,755)

%files -f Tajik.lang Tajik
%defattr(644,root,root,755)

%files -f Ukrainian.lang Ukrainian
%defattr(644,root,root,755)

%files -f Uzbek.lang Uzbek
%defattr(644,root,root,755)

#%files -f Venda.lang Venda

%files -f Vietnamese.lang Vietnamese
%defattr(644,root,root,755)

%files -f Walloon.lang Walloon
%defattr(644,root,root,755)

#%files -f Xhosa.lang Xhosa

%files -f Simplified_Chinese.lang Simplified_Chinese
%defattr(644,root,root,755)

%files -f Chinese.lang Chinese
%defattr(644,root,root,755)

#%files -f Zulu.lang Zulu
