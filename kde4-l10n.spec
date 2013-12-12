# NOTE
# - easy way to update all sources with new/old locales:
#   lynx -dump ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n | awk '/.tar.bz2$/{printf("Source%d: %s\n", i++, $2)}' | tee out
#   and then:r out in vim and ./builder -a5 the spec

# TODO
# - TOOOOOOOOONS of unpackaged files! NIGHTMARE
# - move LC_SCRIPTS contents to LC_MESSAGES (but patch kde to search from there):
#   /usr/share/locale/ga/LC_SCRIPTS/kdelibs4/kdelibs4.js
#   /usr/share/locale/ja/LC_SCRIPTS/kdelibs4/kdelibs4.js
#   /usr/share/locale/ja/LC_SCRIPTS/kgeography/kgeography.js
#   /usr/share/locale/ko/LC_SCRIPTS/kdelibs4/kdelibs4.js
#   /usr/share/locale/zh_CN/LC_SCRIPTS/kdelibs4/kdelibs4.js

%define		_state		stable

Summary:	K Desktop Environment - international support
Summary(pl.UTF-8):	KDE - wsparcie dla wielu języków
Name:		kde4-l10n
Version:	4.11.4
Release:	1
License:	GPL
Group:		I18n
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-ar-%{version}.tar.xz
# Source0-md5:	9a7a2ddc3e91767d3828ad8c9bc312bf
Source1:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-bg-%{version}.tar.xz
# Source1-md5:	9cec34fa15c25d92dbc19241a8d7ee98
Source2:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-bs-%{version}.tar.xz
# Source2-md5:	631fce1c06264c82acffd26014f592b2
Source3:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-ca-%{version}.tar.xz
# Source3-md5:	8fbbe9f07d9ee434668ff13e2aab14a9
Source4:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-ca@valencia-%{version}.tar.xz
# Source4-md5:	7a70b880417b28ef6980edcb2f4838a6
Source5:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-cs-%{version}.tar.xz
# Source5-md5:	466ee9c982259988b60cd7237568efed
Source6:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-da-%{version}.tar.xz
# Source6-md5:	9f28797a5865d854257a70f0bf58e972
Source7:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-de-%{version}.tar.xz
# Source7-md5:	d79e2becaa457916858b0674fac2e128
Source8:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-el-%{version}.tar.xz
# Source8-md5:	7175cd0ee9139f4c74b9e55046705ca3
Source9:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-en_GB-%{version}.tar.xz
# Source9-md5:	84b182ee3063d3d54bc51dd3667c1fb7
Source10:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-es-%{version}.tar.xz
# Source10-md5:	1695b90dc6a6cb5c37c29a110f361fd1
Source11:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-et-%{version}.tar.xz
# Source11-md5:	741d6b54e8459d1c324d714c2387415d
Source12:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-eu-%{version}.tar.xz
# Source12-md5:	4310edb7d9de5221d998438ed4d91bbb
Source13:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-fa-%{version}.tar.xz
# Source13-md5:	dedae5d91d1b90338761e94784a9cf64
Source14:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-fi-%{version}.tar.xz
# Source14-md5:	0f3b7fd598c4fef2a6e24caeb7c32e28
Source15:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-fr-%{version}.tar.xz
# Source15-md5:	50f0220c369bf49085f57ca61c46b134
Source16:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-ga-%{version}.tar.xz
# Source16-md5:	f31f59c78444c55b2d40a87e0a3d1adf
Source17:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-gl-%{version}.tar.xz
# Source17-md5:	778800d6710f97fc1aa73a4944e6c586
Source18:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-he-%{version}.tar.xz
# Source18-md5:	31efc2f1c1e9394951f1e16aacce5e46
Source19:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-hi-%{version}.tar.xz
# Source19-md5:	a3cfe0b457922ed6159be5a162b77717
Source20:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-hr-%{version}.tar.xz
# Source20-md5:	f906e3283359a9a49a178e725af79b79
Source21:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-hu-%{version}.tar.xz
# Source21-md5:	224a37df9f019de8c898582fc9aad99b
Source22:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-ia-%{version}.tar.xz
# Source22-md5:	b532801eda46f360d49737a1c360b995
Source23:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-is-%{version}.tar.xz
# Source23-md5:	551f66f0a084c5e643f0a42930670f2a
Source24:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-it-%{version}.tar.xz
# Source24-md5:	1508a0628d56bae125d0221ea996d957
Source25:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-ja-%{version}.tar.xz
# Source25-md5:	d0c54b58308cd0cabcec3a53f3a47f82
Source26:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-kk-%{version}.tar.xz
# Source26-md5:	921a794f2678152ea83131ecf184281e
Source27:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-km-%{version}.tar.xz
# Source27-md5:	e13f44fbc42109a3723ec94a9df73d73
Source28:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-ko-%{version}.tar.xz
# Source28-md5:	2d40d33622194733e2337c0585852fc0
Source29:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-lt-%{version}.tar.xz
# Source29-md5:	ef5c839b4efded21d8848ec88224eca7
Source30:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-lv-%{version}.tar.xz
# Source30-md5:	209e12913f5cc24abfe1894388fe7baf
Source31:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-mr-%{version}.tar.xz
# Source31-md5:	4fce1d44d24a96f1f6773616ad1b0b6c
Source32:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-nb-%{version}.tar.xz
# Source32-md5:	044e1eb80b4e98a12d49190aea091698
Source33:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-nds-%{version}.tar.xz
# Source33-md5:	9e61cf81ccfd70c396b2bd2b345038bc
Source34:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-nl-%{version}.tar.xz
# Source34-md5:	3fd640370ccffff59f5c941af00317e5
Source35:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-nn-%{version}.tar.xz
# Source35-md5:	4e11c853e12418a4be34c2192d60e1df
Source36:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-pa-%{version}.tar.xz
# Source36-md5:	16c4290aa0518d566134f66edcadd496
Source37:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-pl-%{version}.tar.xz
# Source37-md5:	b5f75b75372fe3f0951f882b12337974
Source38:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-pt-%{version}.tar.xz
# Source38-md5:	e59e4d1c4de7f5cba560d9b7c3efc5b5
Source39:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-pt_BR-%{version}.tar.xz
# Source39-md5:	3c45311a73f5aaf3ecf65415a66a0122
Source40:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-ro-%{version}.tar.xz
# Source40-md5:	2c34988c90de0ed53c240f8835b12ca9
Source41:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-ru-%{version}.tar.xz
# Source41-md5:	687ebe90b64f4f2f637a28df79cfdf3f
Source42:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-sk-%{version}.tar.xz
# Source42-md5:	1734bffaf5360fc28eb57cb5eb963809
Source43:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-sl-%{version}.tar.xz
# Source43-md5:	fef67699e4f733f7e6fd7245fbf8fe22
Source44:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-sr-%{version}.tar.xz
# Source44-md5:	ae4daf70eef75860ad304568a42f9eb6
Source45:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-sv-%{version}.tar.xz
# Source45-md5:	6790f5ac0028fda25dacfd1eac90fc77
Source46:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-tg-%{version}.tar.xz
# Source46-md5:	2294e23e6b22a4de91611780578b11e8
Source47:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-tr-%{version}.tar.xz
# Source47-md5:	100dbf0a7c605cc3b8d114202640e1a2
Source48:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-ug-%{version}.tar.xz
# Source48-md5:	62c9d96bd158395eec699cc6fca8dd31
Source49:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-uk-%{version}.tar.xz
# Source49-md5:	d69e7dc4c362b454ba98461dac44e74e
Source50:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-vi-%{version}.tar.xz
# Source50-md5:	cd0efd02e9446a525c39359c42455d9e
Source51:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-wa-%{version}.tar.xz
# Source51-md5:	10743ec61bec9a061b71cd68e1789e4b
Source52:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-zh_CN-%{version}.tar.xz
# Source52-md5:	8b55f318204442fc483b17e7161914a9
Source53:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/kde-l10n/kde-l10n-zh_TW-%{version}.tar.xz
# Source53-md5:	7391b5ae87d4cb68ce101c99f3871997
Source100:	%{name}.cmake
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext-devel
BuildRequires:	kde4-kdelibs-devel
#BuildRequires:	libxml2-progs >= 2.4.2
BuildRequires:	perl-modules
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_py_hardlink	1

%description
K Desktop Environment - international support.

%description -l pl.UTF-8
KDE - wsparcie dla wielu języków.

%package Afrikaans
Summary:	K Desktop Environment - Afrikaans language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka afrykanerskiego
Group:		I18n

%description Afrikaans
K Desktop Environment - Afrikaans language support.

%description Afrikaans -l pl.UTF-8
KDE - wsparcie dla języka afrykanerskiego.

%package Arabic
Summary:	K Desktop Environment - Arabic language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka arabskiego
Group:		I18n

%description Arabic
K Desktop Environment - Arabic language support.

%description Arabic -l pl.UTF-8
KDE - wsparcie dla języka arabskiego.

%package Azerbaijani
Summary:	K Desktop Environment - Azerbaijani language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka azerskiego
Group:		I18n

%description Azerbaijani
K Desktop Environment - Azerbaijani language support.

%description Azerbaijani -l pl.UTF-8
KDE - wsparcie dla języka azerskiego.

%package Belarusian
Summary:	K Desktop Environment - Belarusian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka białoruskiego
Group:		I18n

%description Belarusian
K Desktop Environment - Belarusian language support.

%description Belarusian -l pl.UTF-8
KDE - wsparcie dla języka białoruskiego.

%package Bulgarian
Summary:	K Desktop Environment - Bulgarian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka bułgarskiego
Group:		I18n

%description Bulgarian
K Desktop Environment - Bulgarian language support.

%description Bulgarian -l pl.UTF-8
KDE - wsparcie dla języka bułgarskiego.

%package Bengali
Summary:	K Desktop Environment - Bengali language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka bengalskiego
Group:		I18n

%description Bengali
K Desktop Environment - Bengali language support.

%description Bengali -l pl.UTF-8
KDE - wsparcie dla języka bengalskiego.

%package Breton
Summary:	K Desktop Environment - Breton language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka bretońskiego
Group:		I18n

%description Breton
K Desktop Environment - Breton language support.

%description Breton -l pl.UTF-8
KDE - wsparcie dla języka bretońskiego.

%package Bosnian
Summary:	K Desktop Environment - Bosnian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka bośniackiego
Group:		I18n

%description Bosnian
K Desktop Environment - Bosnian language support.

%description Bosnian -l pl.UTF-8
KDE - wsparcie dla języka bośniackiego.

%package Catalan
Summary:	K Desktop Environment - Catalan language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka katalońskiego
Group:		I18n

%description Catalan
K Desktop Environment - Catalan language support.

%description Catalan -l pl.UTF-8
KDE - wsparcie dla języka katalońskiego.

%package Catalan-Valencian
Summary:	K Desktop Environment - Catalan Valencian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka katalońskiego walenckiego
Group:		I18n

%description Catalan-Valencian
K Desktop Environment - Catalan Valencian language support.

%description Catalan-Valencian -l pl.UTF-8
KDE - wsparcie dla języka katalońskiego walenckiego.

%package Czech
Summary:	K Desktop Environment - Czech language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka czeskiego
Group:		I18n

%description Czech
K Desktop Environment - Czech language support.

%description Czech -l pl.UTF-8
KDE - wsparcie dla języka czeskiego.

%package Kashubian
Summary:	K Desktop Environment - Kashubian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka kaszubskiego
Group:		I18n

%description Kashubian
K Desktop Environment - Kashubian language support.

%description Kashubian -l pl.UTF-8
KDE - wsparcie dla języka kaszubskiego.

%package Cymraeg
Summary:	K Desktop Environment - Cymraeg language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka walijskiego
Group:		I18n

%description Cymraeg
K Desktop Environment - Cymraeg language support.

%description Cymraeg -l pl.UTF-8
KDE - wsparcie dla języka walijskiego.

%package Danish
Summary:	K Desktop Environment - Danish language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka duńskiego
Group:		I18n

%description Danish
K Desktop Environment - Danish language support.

%description Danish -l pl.UTF-8
KDE - wsparcie dla języka duńskiego.

%package German
Summary:	K Desktop Environment - German language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka niemieckiego
Group:		I18n

%description German
K Desktop Environment - German language support.

%description German -l pl.UTF-8
KDE - wsparcie dla języka niemieckiego.

%package Greek
Summary:	K Desktop Environment - Greek language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka greckiego
Group:		I18n

%description Greek
K Desktop Environment - Greek language support.

%description Greek -l pl.UTF-8
KDE - wsparcie dla języka greckiego.

%package English
Summary:	K Desktop Environment - English language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka angielskiego
Group:		I18n

%description English
K Desktop Environment - English language support.

%description English -l pl.UTF-8
KDE - wsparcie dla języka angielskiego.

%package English_UK
Summary:	K Desktop Environment - K Desktop Environment - English (UK) language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka angielskiego (odmiany brytyjskiej)
Group:		I18n

%description English_UK
K Desktop Environment - English (UK) language support.

%description English_UK -l pl.UTF-8
KDE - wsparcie dla języka angielskiego (odmiany brytyjskiej).

%package Esperanto
Summary:	K Desktop Environment - Esperanto language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka esperanto
Group:		I18n

%description Esperanto
K Desktop Environment - Esperanto language support.

%description Esperanto -l pl.UTF-8
KDE - wsparcie dla języka esperanto.

%package Spanish
Summary:	K Desktop Environment - Spanish language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka hiszpańskiego
Group:		I18n

%description Spanish
K Desktop Environment - Spanish language support.

%description Spanish -l pl.UTF-8
KDE - wsparcie dla języka hiszpańskiego.

%package Estonian
Summary:	K Desktop Environment - Estonian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka estońskiego
Group:		I18n

%description Estonian
K Desktop Environment - Estonian language support.

%description Estonian -l pl.UTF-8
KDE - wsparcie dla języka estońskiego.

%package Basque
Summary:	K Desktop Environment - Basque language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka baskijskiego
Group:		I18n

%description Basque
K Desktop Environment - Basque language support.

%description Basque -l pl.UTF-8
KDE - wsparcie dla języka baskijskiego.

%package Farsi
Summary:	K Desktop Environment - Farsi language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka perskiego (farsi)
Group:		I18n

%description Farsi
K Desktop Environment - Farsi language support.

%description Farsi -l pl.UTF-8
KDE - wsparcie dla języka perskiego (farsi).

%package Finnish
Summary:	K Desktop Environment - Finnish language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka fińskiego
Group:		I18n

%description Finnish
K Desktop Environment - Finnish language support.

%description Finnish -l pl.UTF-8
KDE - wsparcie dla języka fińskiego.

%package French
Summary:	K Desktop Environment - French language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka francuskiego
Group:		I18n

%description French
K Desktop Environment - French language support.

%description French -l pl.UTF-8
KDE - wsparcie dla języka francuskiego.

%package Frisian
Summary:	K Desktop Environment - Frisian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka fryzyjskiego
Group:		I18n

%description Frisian
K Desktop Environment - Frisian language support.

%description Frisian -l pl.UTF-8
KDE - wsparcie dla języka fryzyjskiego.

%package Irish
Summary:	K Desktop Environment - Irish language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka irlandzkiego
Group:		I18n

%description Irish
K Desktop Environment - Irish language support.

%description Irish -l pl.UTF-8
KDE - wsparcie dla języka irlandzkiego.

%package Galician
Summary:	K Desktop Environment - Galician language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka galicyjskiego
Group:		I18n

%description Galician
K Desktop Environment - Galician language support.

%description Galician -l pl.UTF-8
KDE - wsparcie dla języka galicyjskiego.

%package Hindi
Summary:	K Desktop Environment - Hindi language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka hindi
Group:		I18n

%description Hindi
K Desktop Environment - Hindi language support.

%description Hindi -l pl.UTF-8
KDE - wsparcie dla języka hindi.

%package Hebrew
Summary:	K Desktop Environment - Hebrew language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka hebrajskiego
Group:		I18n

%description Hebrew
K Desktop Environment - Hebrew language support.

%description Hebrew -l pl.UTF-8
KDE - wsparcie dla języka hebrajskiego.

%package Croatian
Summary:	K Desktop Environment - Croatian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka chorwackiego
Group:		I18n

%description Croatian
K Desktop Environment - Croatian language support.

%description Croatian -l pl.UTF-8
KDE - wsparcie dla języka chorwackiego.

%package Upper_Sorbian
Summary:	K Desktop Environment - Upper Sorbian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka górnołużyckiego
Group:		I18n

%description Upper_Sorbian
K Desktop Environment - Upper Sorbian language support.

%description Upper_Sorbian -l pl.UTF-8
KDE - wsparcie dla języka górnołużyckiego.

%package Hungarian
Summary:	K Desktop Environment - Hungarian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka węgierskiego
Group:		I18n

%description Hungarian
K Desktop Environment - Hungarian language support.

%description Hungarian -l pl.UTF-8
KDE - wsparcie dla języka węgierskiego.

%package Interlingua
Summary:	K Desktop Environment - Interlingua locale support
Summary(pl.UTF-8):	KDE - wsparcie dla języka lokalizacji Interlingua
Group:		I18n

%description Interlingua
K Desktop Environment - Interlingua (International Auxiliary Language
Association) locale support.

%package Indonesian
Summary:	K Desktop Environment - Indonesian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka indonezyjskiego
Group:		I18n

%description Indonesian
K Desktop Environment - Indonesian language support.

%description Indonesian -l pl.UTF-8
KDE - wsparcie dla języka indonezyjskiego.

%package Icelandic
Summary:	K Desktop Environment - Icelandic language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka islandzkiego
Group:		I18n

%description Icelandic
K Desktop Environment - Icelandic language support.

%description Icelandic -l pl.UTF-8
KDE - wsparcie dla języka islandzkiego.

%package Italian
Summary:	K Desktop Environment - Italian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka włoskiego
Group:		I18n

%description Italian
K Desktop Environment - Italian language support.

%description Italian -l pl.UTF-8
KDE - wsparcie dla języka włoskiego.

%package Japanese
Summary:	K Desktop Environment - Japanese language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka japońskiego
Group:		I18n

%description Japanese
K Desktop Environment - Japanese language support.

%description Japanese -l pl.UTF-8
KDE - wsparcie dla języka japońskiego.

%package Kazakh
Summary:	K Desktop Environment - Kazakh language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka kazaskiego
Group:		I18n

%description Kazakh
K Desktop Environment - Kazakh language support.

%description Kazakh -l pl.UTF-8
KDE - wsparcie dla języka kazaskiego.

%package Khmer
Summary:	K Desktop Environment - Khmer language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka khmerskiego
Group:		I18n

%description Khmer
K Desktop Environment - Khmer language support.

%description Khmer -l pl.UTF-8
KDE - wsparcie dla języka khmerskiego.

%package Kinyarwanda
Summary:	K Desktop Environment - Kinyarwanda language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka kinya-ruanda
Group:		I18n

%description Kinyarwanda
K Desktop Environment - Kinyarwanda language support.

%description Kinyarwanda -l pl.UTF-8
KDE - wsparcie dla języka kinya-ruanda.

%package Korean
Summary:	K Desktop Environment - Korean language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka koreańskiego
Group:		I18n

%description Korean
K Desktop Environment - Korean language support.

%description Korean -l pl.UTF-8
KDE - wsparcie dla języka koreańskiego.

%package Kurdish
Summary:	K Desktop Environment - Kurdish language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka kurdyjskiego
Group:		I18n

%description Kurdish
K Desktop Environment - Kurdish language support.

%description Kurdish -l pl.UTF-8
KDE - wsparcie dla języka kurdyjskiego.

%package Lithuanian
Summary:	K Desktop Environment - Lithuanian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka litewskiego
Group:		I18n

%description Lithuanian
K Desktop Environment - Lithuanian language support.

%description Lithuanian -l pl.UTF-8
KDE - Wsparcie dla języka litewskiego.

%package Lao
Summary:	K Desktop Environment - Lao language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka laotańskiego
Group:		I18n

%description Lao
K Desktop Environment - lao language support.

%description Lao -l pl.UTF-8
KDE - wsparcie dla języka laotańskiego.

%package Latvian
Summary:	K Desktop Environment - Latvian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka łotewskiego
Group:		I18n

%description Latvian
K Desktop Environment - Latvian language support.

%description Latvian -l pl.UTF-8
KDE - wsparcie dla języka łotewskiego.

%package Maori
Summary:	K Desktop Environment - Maori language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka maoryjskiego
Group:		I18n

%description Maori
K Desktop Environment - Maori language support.

%description Maori -l pl.UTF-8
KDE - wsparcie dla języka maoryjskiego.

%package Macedonian
Summary:	K Desktop Environment - Macedonian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka macedońskiego
Group:		I18n

%description Macedonian
K Desktop Environment - Macedonian language support.

%description Macedonian -l pl.UTF-8
KDE - wsparcie dla języka macedońskiego.

%package Malayalam
Summary:	K Desktop Environment - Malayalam language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka malajalam
Group:		I18n

%description Malayalam
K Desktop Environment - Malayalam language support.

%description Malayalam -l pl.UTF-8
KDE - wsparcie dla języka malajalam.

%package Maltese
Summary:	K Desktop Environment - Maltese language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka maltańskiego
Group:		I18n

%description Maltese
K Desktop Environment - Maltese language support.

%description Maltese -l pl.UTF-8
KDE - wsparcie dla języka maltańskiego.

%package Marathi
Summary:	K Desktop Environment - Marathi language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka marathi
Group:		I18n

%description Marathi
K Desktop Environment - Marathi language support.

%description Marathi -l pl.UTF-8
KDE - wsparcie dla języka marathi.

%package Mongolian
Summary:	K Desktop Environment - Mongolian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka mongolskiego
Group:		I18n

%description Mongolian
K Desktop Environment - Mongolian language support.

%description Mongolian -l pl.UTF-8
KDE - wsparcie dla języka mongolskiego.

%package Low_Saxon
Summary:	K Desktop Environment - Low Saxon language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka dolnosaksońskiego
Group:		I18n

%description Low_Saxon
K Desktop Environment - Low Saxon language support.

%description Low_Saxon -l pl.UTF-8
KDE - wsparcie dla języka dolnosaksońskiego.

%package Nepali
Summary:	K Desktop Environment - Nepali language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka nepalskiego
Group:		I18n

%description Nepali
K Desktop Environment - Nepali language support.

%description Nepali -l pl.UTF-8
KDE - wsparcie dla języka nepalskiego.

%package Dutch
Summary:	K Desktop Environment - Dutch language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka holenderskiego
Group:		I18n

%description Dutch
K Desktop Environment - Dutch language support.

%description Dutch -l pl.UTF-8
KDE - wsparcie dla języka holenderskiego.

%package Norwegian_Bokmaal
Summary:	K Desktop Environment - Norwegian (Bokmaal) language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka norweskiego (odmiany bokmaal)
Group:		I18n

%description Norwegian_Bokmaal
K Desktop Environment - Norwegian (Bokmaal) language support.

%description Norwegian_Bokmaal -l pl.UTF-8
KDE - wsparcie dla języka norweskiego (odmiany bokmaal).

%package Norwegian_Nynorsk
Summary:	K Desktop Environment - Norwegian (Nynorsk) language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka norweskiego (odmiany nynorsk)
Group:		I18n

%description Norwegian_Nynorsk
K Desktop Environment - Norwegian (Nynorsk) language support.

%description Norwegian_Nynorsk -l pl.UTF-8
KDE - wsparcie dla języka norweskiego (odmiany nynorsk).

%package Northern_Sotho
Summary:	K Desktop Environment - Northern Sotho language support
Summary(pl.UTF-8):	KDE - wsparcie dla północnej odmiany języka ludu Soto
Group:		I18n

%description Northern_Sotho
K Desktop Environment - Northern Sotho language support.

%description Northern_Sotho -l pl.UTF-8
KDE - wsparcie dla północnej odmiany języka ludu Soto.

%package Gascon_Occitan
Summary:	K Desktop Environment - Occitan (Gascon) language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka oksytańskiego (dialektu gaskońskiego)
Group:		I18n

%description Gascon_Occitan
K Desktop Environment - Occitan (Gascon) language support.

%description Gascon_Occitan -l pl.UTF-8
KDE - wsparcie dla języka oksytańskiego (dialektu gaskońskiego).

%package Punjabi
Summary:	K Desktop Environment - Punjabi language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka pendżabskiego
Group:		I18n

%description Punjabi
K Desktop Environment - Punjabi language support.

%description Punjabi -l pl.UTF-8
KDE - wsparcie dla języka pendżabskiego.

%package Polish
Summary:	K Desktop Environment - Polish language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka polskiego
Group:		I18n

%description Polish
K Desktop Environment - Polish language support.

%description Polish -l pl.UTF-8
KDE - wsparcie dla języka polskiego.

%package Portuguese
Summary:	K Desktop Environment - Portuguese language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka portugalskiego
Group:		I18n

%description Portuguese
K Desktop Environment - Portuguese language support.

%description Portuguese -l pl.UTF-8
KDE - wsparcie dla języka portugalskiego.

%package Brazil_Portuguese
Summary:	K Desktop Environment - Portuguese (Brazil) language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka portugalskiego (odmiany brazylijskiej)
Group:		I18n

%description Brazil_Portuguese
K Desktop Environment - Portuguese (Brazil) language support.

%description Brazil_Portuguese -l pl.UTF-8
KDE - wsparcie dla języka portugalskiego (odmiany brazylijskiej).

%package Romanian
Summary:	K Desktop Environment - Romanian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka rumuńskiego
Group:		I18n

%description Romanian
K Desktop Environment - Romanian language support.

%description Romanian -l pl.UTF-8
KDE - wsparcie dla języka rumuńskiego.

%package Russian
Summary:	K Desktop Environment - Russian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka rosyjskiego
Group:		I18n

%description Russian
K Desktop Environment - Russian language support.

%description Russian -l pl.UTF-8
KDE - wsparcie dla języka rosyjskiego.

%package Swati
Summary:	K Desktop Environment - Swati language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka swati
Group:		I18n

%description Swati
K Desktop Environment - Swati language support.

%description Swati -l pl.UTF-8
KDE - wsparcie dla języka swati.

%package Northern_Sami
Summary:	K Desktop Environment - Northern Sami language support
Summary(pl.UTF-8):	KDE - wsparcie dla północnego języka saami (lapońskiego)
Group:		I18n

%description Northern_Sami
K Desktop Environment - Northern Sami language support.

%description Northern_Sami -l pl.UTF-8
KDE - wsparcie dla północnego języka saami (lapońskiego).

%package Slovak
Summary:	K Desktop Environment - Slovak language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka słowackiego
Group:		I18n

%description Slovak
K Desktop Environment - Slovak language support.

%description Slovak -l pl.UTF-8
KDE - wsparcie dla języka słowackiego.

%package Slovenian
Summary:	K Desktop Environment - Slovenian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka słoweńskiego
Group:		I18n

%description Slovenian
K Desktop Environment - Slovenian language support.

%description Slovenian -l pl.UTF-8
KDE - wsparcie dla języka słoweńskiego.

%package Serbian
Summary:	K Desktop Environment - Serbian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka serbskiego
Group:		I18n

%description Serbian
K Desktop Environment - Serbian language support.

%description Serbian -l pl.UTF-8
KDE - wsparcie dla języka serbskiego.

%package Sinhalese
Summary:	K Desktop Environment - Sinhalese language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka cejlońskiego
Group:		I18n

%description Sinhalese
K Desktop Environment - Sinhalese language support.

%description Sinhalese -l pl.UTF-8
KDE - wsparcie dla języka cejlońskiego.

%package Swedish
Summary:	K Desktop Environment - Swedish language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka szwedzkiego
Group:		I18n

%description Swedish
K Desktop Environment - Swedish language support.

%description Swedish -l pl.UTF-8
KDE - wsparcie dla języka szwedzkiego.

%package Tajik
Summary:	K Desktop Environment - Tajik language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka tadżyckiego
Group:		I18n

%description Tajik
K Desktop Environment - Tajik language support.

%description Tajik -l pl.UTF-8
KDE - wsparcie dla języka tadżyckiego.

%package Tamil
Summary:	K Desktop Environment - Tamil language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka tamilskiego
Group:		I18n

%description Tamil
K Desktop Environment - Tamil language support.

%description Tamil -l pl.UTF-8
KDE - wsparcie dla języka tamilskiego.

%package Telugu
Summary:	K Desktop Environment - Telugu language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka telugu
Group:		I18n

%description Telugu
K Desktop Environment - Telugu language support.

%description Telugu -l pl.UTF-8
KDE - wsparcie dla języka telugu.

%package Thai
Summary:	K Desktop Environment - Thai language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka tajlandzkiego
Group:		I18n

%description Thai
K Desktop Environment - Thai language support.

%description Thai -l pl.UTF-8
KDE - wsparcie dla języka tajlandzkiego.

%package Turkish
Summary:	K Desktop Environment - Turkish language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka tureckiego
Group:		I18n

%description Turkish
K Desktop Environment - Turkish language support.

%description Turkish -l pl.UTF-8
KDE - wsparcie dla języka tureckiego.

%package Uyghur
Summary:	K Desktop Environment - Uyghur language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka uigurskiego
Group:		I18n

%description Uyghur
K Desktop Environment - Ukrainian language support.

%description Uyghur -l pl.UTF-8
KDE - wsparcie dla języka uigurskiego.

%package Ukrainian
Summary:	K Desktop Environment - Ukrainian language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka ukraińskiego
Group:		I18n

%description Ukrainian
K Desktop Environment - Ukrainian language support.

%description Ukrainian -l pl.UTF-8
KDE - wsparcie dla języka ukraińskiego.

%package Urdu
Summary:	K Desktop Environment - Urdu language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka urdu
Group:		I18n

%description Urdu
K Desktop Environment - Urdu language support.

%description Urdu -l pl.UTF-8
KDE - wsparcie dla języka urdu.

%package Uzbek
Summary:	K Desktop Environment - Uzbek language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka uzbeckiego
Group:		I18n

%description Uzbek
K Desktop Environment - Uzbek language support.

%description Uzbek -l pl.UTF-8
KDE - wsparcie dla języka uzbeckiego.

%package Venda
Summary:	K Desktop Environment - Venda language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka venda
Group:		I18n

%description Venda
K Desktop Environment - Venda language support.

%description Venda -l pl.UTF-8
KDE - wsparcie dla języka venda.

%package Vietnamese
Summary:	K Desktop Environment - Vietnamese language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka wietnamskiego
Group:		I18n

%description Vietnamese
K Desktop Environment - Vietnamese language support.

%description Vietnamese -l pl.UTF-8
KDE - wsparcie dla języka wietnamskiego.

%package Walloon
Summary:	K Desktop Environment - Walloon language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka walońskiego
Group:		I18n

%description Walloon
K Desktop Environment - Walloon language support.

%description Walloon -l pl.UTF-8
KDE - wsparcie dla języka walońskiego.

%package Xhosa
Summary:	K Desktop Environment - Xhosa language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka khosa
Group:		I18n

%description Xhosa
K Desktop Environment - Xhosa language support.

%description Xhosa -l pl.UTF-8
KDE - wsparcie dla języka khosa.

%package Simplified_Chinese
Summary:	K Desktop Environment - simplified Chinese language support
Summary(pl.UTF-8):	KDE - wsparcie dla uproszczonego języka chińskiego
Group:		I18n

%description Simplified_Chinese
K Desktop Environment - simplified Chinese language support.

%description Simplified_Chinese -l pl.UTF-8
KDE - wsparcie dla uproszczonego języka chińskiego.

%package Chinese
Summary:	K Desktop Environment - Chinese language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka chińskiego
Group:		I18n

%description Chinese
K Desktop Environment - Chinese language support.

%description Chinese -l pl.UTF-8
KDE - wsparcie dla języka chińskiego.

%package Zulu
Summary:	K Desktop Environment - Zulu language support
Summary(pl.UTF-8):	KDE - wsparcie dla języka zuluskiego
Group:		I18n

%description Zulu
K Desktop Environment - Zulu language support.

%description Zulu -l pl.UTF-8
KDE - wsparcie dla języka zuluskiego.

%prep
#%%setup -qcT %(seq -f '-a %g' 0 51 |sed -e 's/-a 14$//;s/-a 20$//;s/-a 37$//;s/-a 3$//;s/-a 23$//;s/-a 24$//;/^$/d' | xargs)
%setup -qcT %(seq -f '-a %g' 0 53 | xargs)

install %{SOURCE100} ./CMakeLists.txt

%build
install -d build
cd build
%cmake \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_VERBOSE_MAKEFILE=ON \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
	..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
cd build
if [ ! -f makeinstall.stamp -o ! -d $RPM_BUILD_ROOT ]; then
	rm -rf makeinstall.stamp installed.stamp $RPM_BUILD_ROOT

	%{__make} install \
		DESTDIR=$RPM_BUILD_ROOT

	touch makeinstall.stamp
fi

if [ ! -f installed.stamp ]; then
	# remove empty language catalogs (= 1 message only)
	find $RPM_BUILD_ROOT%{_localedir} -type f -name '*.mo' | xargs file | egrep ', 1 messages$' | cut -d: -f1 | xargs rm -vf

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
	if [ -d "$RPM_BUILD_ROOT%{_localedir}/$lang" ]; then
		echo "%lang($lang) %{_localedir}/$lang/[cef]*"
		echo "%lang($lang) %{_localedir}/$lang/LC_MESSAGES/*.mo"
	fi

	# share/locale/(%%lang)/LC_SCRIPTS
	if [ -d "$RPM_BUILD_ROOT%{_localedir}/$lang/LC_SCRIPTS" ]; then
		echo "%lang($lang) %dir %{_localedir}/$lang/LC_SCRIPTS"
		echo "%lang($lang) %{_localedir}/$lang/LC_SCRIPTS/*"
	fi

	# share/apps/amor/tips-(%%lang)
	if [ -f "$RPM_BUILD_ROOT%{_datadir}/apps/amor/tips-$lang" ]; then
		echo "%dir %{_datadir}/apps/amor"
		echo "%lang($lang) %{_datadir}/apps/amor/tips-$lang"
	fi

	# share/apps/katepart/syntax/logohighlightstyle.(%%lang).xml
	if [ -f "$RPM_BUILD_ROOT%{_datadir}/apps/katepart/syntax/logohighlightstyle.$lang.xml" ]; then
		echo "%lang($lang) %{_datadir}/apps/katepart/syntax/logohighlightstyle.$lang.xml"
	fi

	# share/apps/ktuberling/sounds/(%%lang)
	if [ -d "$RPM_BUILD_ROOT%{_datadir}/apps/ktuberling/sounds/$lang" ]; then
		#echo "%dir %{_datadir}/apps/ktuberling"
		echo "%dir %{_datadir}/apps/ktuberling/sounds"
		echo "%lang($lang) %{_datadir}/apps/ktuberling/sounds/$lang"
	fi

	# share/apps/khangman/(%lang).txt
	if [ -f "$RPM_BUILD_ROOT%{_datadir}/apps/khangman/$lang.txt" ]; then
		echo "%dir %{_datadir}/apps/khangman"
		echo "%lang($lang) %{_datadir}/apps/khangman/$lang.txt"
	fi

	# share/apps/khangman/data/(%lang)
	if [ -d "$RPM_BUILD_ROOT%{_datadir}/apps/khangman/data/$lang" ]; then
		echo "%dir %{_datadir}/apps/khangman/data"
		echo "%lang($lang) %{_datadir}/apps/khangman/data/$lang"
	fi

	# share/apps/klatin/data/vocabs/(%lang)
	if [ -d "$RPM_BUILD_ROOT%{_datadir}/apps/klatin/data/vocabs/$lang" ]; then
		echo "%dir %{_datadir}/apps/klatin"
		echo "%dir %{_datadir}/apps/klatin/data"
		echo "%dir %{_datadir}/apps/klatin/data/vocabs"
		echo "%lang($lang) %{_datadir}/apps/klatin/data/vocabs/$lang"
	fi

	# share/apps/klettres/(%lang)
	if [ -d "$RPM_BUILD_ROOT%{_datadir}/apps/klettres/$lang" ]; then
		echo "%dir %{_datadir}/apps/klettres"
		echo "%lang($lang) %{_datadir}/apps/klettres/$lang"
	fi

	# share/apps/kturtle/data/logokeywords.(%lang).xml
	if [ -f "$RPM_BUILD_ROOT%{_datadir}/apps/kturtle/data/logokeywords.$lang.xml" ]; then
		echo "%dir %{_datadir}/apps/kturtle"
		echo "%dir %{_datadir}/apps/kturtle/data"
		echo "%lang($lang) %{_datadir}/apps/kturtle/data/logokeywords.$lang.xml"
	fi

	# share/apps/kturtle/examples/(%lang)
	if [ -d "$RPM_BUILD_ROOT%{_datadir}/apps/kturtle/examples/$lang" ]; then
		echo "%dir %{_datadir}/apps/kturtle/examples"
		echo "%lang($lang) %{_datadir}/apps/kturtle/examples/$lang"
	fi

	# share/apps/kanagram/data/et/elukutsed.kvtml
	if [ -d "$RPM_BUILD_ROOT%{_datadir}/apps/kanagram/data/$lang" ]; then
		echo "%dir %{_datadir}/apps/kanagram"
		echo "%dir %{_datadir}/apps/kanagram/data"
		echo "%lang($lang) %{_datadir}/apps/kanagram/data/$lang"
	fi

	if [ -d "$RPM_BUILD_ROOT%{_datadir}/apps/kvtml/$lang" ]; then
		echo "%dir %{_datadir}/apps/kvtml"
		echo "%lang($lang) %{_datadir}/apps/kvtml/$lang"
	fi

	if [ -f "$RPM_BUILD_ROOT%{_datadir}/apps/ktuberling/sounds/$lang.soundtheme" ]; then
		echo "%lang($lang) %{_datadir}/apps/ktuberling/sounds/$lang.soundtheme"
	fi

	touch $lang.ok
}

rm -f *.lang *.cache __find.* *.ok
find $RPM_BUILD_ROOT -name \*sr@ijekavian\* |xargs rm -rf

FindLang af > ../Afrikaans.lang
FindLang ar > ../Arabic.lang
FindLang az > ../Azerbaijani.lang
FindLang be > ../Belarusian.lang
FindLang bg > ../Bulgarian.lang
FindLang bn > ../Bengali.lang
FindLang br > ../Breton.lang
FindLang bs > ../Bosnian.lang
FindLang ca > ../Catalan.lang
FindLang ca@valencia > ../Catalan-Valencian.lang
FindLang cs > ../Czech.lang
FindLang csb > ../Kashubian.lang
FindLang cy > ../Cymraeg.lang
FindLang da > ../Danish.lang
FindLang de > ../German.lang
FindLang el > ../Greek.lang
#FindLang en > ../English.lang
FindLang en_GB > ../English_UK.lang
#FindLang eo > ../Esperanto.lang
FindLang es > ../Spanish.lang
FindLang et > ../Estonian.lang
FindLang eu > ../Basque.lang
FindLang fa > ../Farsi.lang
FindLang fi > ../Finnish.lang
FindLang fr > ../French.lang
#FindLang fy > ../Frisian.lang
FindLang ga > ../Irish.lang
FindLang gl > ../Galician.lang
FindLang he > ../Hebrew.lang
FindLang hi > ../Hindi.lang
FindLang hr > ../Croatian.lang
#FindLang hsb > ../Upper_Sorbian.lang
FindLang hu > ../Hungarian.lang
#FindLang id > ../Indonesian.lang
FindLang ia > ../Interlingua.lang
FindLang is > ../Icelandic.lang
FindLang it > ../Italian.lang
FindLang ja > ../Japanese.lang
FindLang kk > ../Kazakh.lang
FindLang km > ../Khmer.lang
FindLang ko > ../Korean.lang
#FindLang ku > ../Kurdish.lang
FindLang lt > ../Lithuanian.lang
FindLang lv > ../Latvian.lang
#FindLang mi > ../Maori.lang
FindLang mk > ../Macedonian.lang
FindLang ml > ../Malayalam.lang
FindLang mn > ../Mongolian.lang
FindLang mr > ../Marathi.lang
#FindLang ms > ../Malay.lang
#FindLang mt > ../Maltese.lang
FindLang nb > ../Norwegian_Bokmaal.lang
FindLang nds > ../Low_Saxon.lang
FindLang ne > ../Nepali.lang
FindLang nl > ../Dutch.lang
FindLang nn > ../Norwegian_Nynorsk.lang
FindLang pa > ../Punjabi.lang
#FindLang nso > ../Northern_Sotho.lang
#FindLang oc > ../Gascon_Occitan.lang
FindLang pl > ../Polish.lang
FindLang pt > ../Portuguese.lang
FindLang pt_BR > ../Brazil_Portuguese.lang
FindLang ro > ../Romanian.lang
FindLang rw > ../Kinyarwanda.lang
FindLang ru > ../Russian.lang
FindLang ss > ../Swati.lang
FindLang si > ../Sinhalese.lang
FindLang se > ../Northern_Sami.lang
FindLang sk > ../Slovak.lang
FindLang sl > ../Slovenian.lang
FindLang sr > ../Serbian.lang
FindLang sr@latin >> ../Serbian.lang
mv ../Serbian.lang ../Serbian.lang.orig
cat ../Serbian.lang.orig | sort | uniq > ../Serbian.lang
FindLang sv > ../Swedish.lang
#FindLang ta > ../Tamil.lang
FindLang te > ../Telugu.lang
FindLang tg > ../Tajik.lang
FindLang th > ../Thai.lang
FindLang tr > ../Turkish.lang
FindLang ug > ../Uyghur.lang
FindLang uk > ../Ukrainian.lang
FindLang ur > ../Urdu.lang
FindLang uz > ../Uzbek.lang
#FindLang ven > ../Venda.lang
FindLang vi > ../Vietnamese.lang
FindLang wa > ../Walloon.lang
#FindLang xh > ../Xhosa.lang
FindLang zh_CN > ../Simplified_Chinese.lang
FindLang zh_TW > ../Chinese.lang
#FindLang zu > ../Zulu.lang

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

%files -f Afrikaans.lang Afrikaans
%defattr(644,root,root,755)

%files -f Arabic.lang Arabic
%defattr(644,root,root,755)

%files -f Azerbaijani.lang Azerbaijani
%defattr(644,root,root,755)

%files -f Belarusian.lang Belarusian
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
%{_mandir}/ca/man1/*.1*
%{_mandir}/ca/man6/*.6*
%{_mandir}/ca/man7/*.7*
%{_mandir}/ca/man8/*.8*

%files -f Catalan-Valencian.lang Catalan-Valencian
%defattr(644,root,root,755)

%files -f Czech.lang Czech
%defattr(644,root,root,755)

%files -f Cymraeg.lang Cymraeg
%defattr(644,root,root,755)

%files -f Danish.lang Danish
%defattr(644,root,root,755)
%{_mandir}/da/man1/*.1*
%{_mandir}/da/man6/*.6*

%files -f German.lang German
%defattr(644,root,root,755)
%{_mandir}/de/man1/*.1*
%{_mandir}/de/man6/*.6*
%{_mandir}/de/man7/*.7*
%{_mandir}/de/man8/*.8*

%files -f Greek.lang Greek
%defattr(644,root,root,755)
%{_mandir}/el/man1/*.1*

# %files -f English.lang English

%files -f English_UK.lang English_UK
%defattr(644,root,root,755)

#%files -f Esperanto.lang Esperanto
#%defattr(644,root,root,755)

%files -f Spanish.lang Spanish
%defattr(644,root,root,755)
%{_mandir}/es/man1/*.1*
%{_mandir}/es/man6/*.6*
%{_mandir}/es/man7/*.7*
%{_mandir}/es/man8/*.8*

%files -f Estonian.lang Estonian
%defattr(644,root,root,755)
%{_mandir}/et/man1/*.1*
%{_mandir}/et/man6/*.6*
%{_mandir}/et/man7/*.7*
%{_mandir}/et/man8/*.8*

%files -f Basque.lang Basque
%defattr(644,root,root,755)

%files -f Farsi.lang Farsi
%defattr(644,root,root,755)

%files -f Finnish.lang Finnish
%defattr(644,root,root,755)

%files -f French.lang French
%defattr(644,root,root,755)
%{_mandir}/fr/man1/*.1*
%{_mandir}/fr/man6/*.6*
%{_mandir}/fr/man7/*.7*
%{_mandir}/fr/man8/*.8*

#%files -f Frisian.lang Frisian
#%defattr(644,root,root,755)

%files -f Irish.lang Irish
%defattr(644,root,root,755)

%files -f Galician.lang Galician
%defattr(644,root,root,755)
%{_mandir}/gl/man1/*.1*
%{_mandir}/gl/man6/*.6*
%{_mandir}/gl/man7/*.7*
%{_mandir}/gl/man8/*.8*

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

%files -f Interlingua.lang Interlingua
%defattr(644,root,root,755)

%files -f Italian.lang Italian
%defattr(644,root,root,755)
%{_mandir}/it/man1/*.1*
%{_mandir}/it/man6/*.6*
%{_mandir}/it/man7/*.7*
%{_mandir}/it/man8/*.8*

%files -f Japanese.lang Japanese
%defattr(644,root,root,755)

%files -f Kazakh.lang Kazakh
%defattr(644,root,root,755)

%files -f Khmer.lang Khmer
%defattr(644,root,root,755)

%files -f Korean.lang Korean
%defattr(644,root,root,755)

#%files -f Kurdish.lang Kurdish
#%defattr(644,root,root,755)

%files -f Kashubian.lang Kashubian
%defattr(644,root,root,755)

%files -f Lithuanian.lang Lithuanian
%defattr(644,root,root,755)
%{_mandir}/lt/man1/*.1*
%{_mandir}/lt/man8/*.8*

%files -f Kinyarwanda.lang Kinyarwanda
%defattr(644,root,root,755)

%files -f Latvian.lang Latvian
%defattr(644,root,root,755)

#%files -f Maltese.lang Maltese

%files -f Mongolian.lang Mongolian
%defattr(644,root,root,755)

#%files -f Maori.lang Maori

%files -f Macedonian.lang Macedonian
%defattr(644,root,root,755)

%files -f Marathi.lang Marathi
%defattr(644,root,root,755)

%files -f Malayalam.lang Malayalam
%defattr(644,root,root,755)

%files -f Low_Saxon.lang Low_Saxon
%defattr(644,root,root,755)

%files -f Nepali.lang Nepali
%defattr(644,root,root,755)

%files -f Dutch.lang Dutch
%defattr(644,root,root,755)
%{_mandir}/nl/man1/*.1*
%{_mandir}/nl/man6/*.6*
%{_mandir}/nl/man7/*.7*
%{_mandir}/nl/man8/*.8*

%files -f Norwegian_Bokmaal.lang Norwegian_Bokmaal
%defattr(644,root,root,755)
%{_mandir}/nb/man1/*.1*

%files -f Norwegian_Nynorsk.lang Norwegian_Nynorsk
%defattr(644,root,root,755)

#%files -f Northern_Sotho.lang Northern_Sotho

#%files -f Gascon_Occitan.lang Gascon_Occitan

%files -f Punjabi.lang Punjabi
%defattr(644,root,root,755)

%files -f Polish.lang Polish
%defattr(644,root,root,755)
%{_mandir}/pl/man1/*.1*
%{_mandir}/pl/man6/*.6*
%{_mandir}/pl/man8/*.8*

%files -f Portuguese.lang Portuguese
%defattr(644,root,root,755)
%{_mandir}/pt/man1/*.1*
%{_mandir}/pt/man6/*.6*
%{_mandir}/pt/man7/*.7*
%{_mandir}/pt/man8/*.8*

%files -f Brazil_Portuguese.lang Brazil_Portuguese
%defattr(644,root,root,755)
%{_mandir}/pt_BR/man1/*.1*
%{_mandir}/pt_BR/man6/*.6*
%{_mandir}/pt_BR/man7/*.7*
%{_mandir}/pt_BR/man8/*.8*

%files -f Romanian.lang Romanian
%defattr(644,root,root,755)

%files -f Russian.lang Russian
%defattr(644,root,root,755)
%{_mandir}/ru/man1/*.1*
%{_mandir}/ru/man6/*.6*
%{_mandir}/ru/man7/*.7*

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
%{_mandir}/sr/man1/*.1*
%{_mandir}/sr@latin/man1/*.1*

%files -f Sinhalese.lang Sinhalese
%defattr(644,root,root,755)

%files -f Swedish.lang Swedish
%defattr(644,root,root,755)
%{_mandir}/sv/man1/*.1*
%{_mandir}/sv/man6/*.6*
%{_mandir}/sv/man7/*.7*
%{_mandir}/sv/man8/*.8*

#%files -f Tamil.lang Tamil
#%defattr(644,root,root,755)

%files -f Telugu.lang Telugu
%defattr(644,root,root,755)

%files -f Thai.lang Thai
%defattr(644,root,root,755)

%files -f Turkish.lang Turkish
%defattr(644,root,root,755)
%{_mandir}/tr/man1/*.1*
%{_mandir}/tr/man7/*.7*

%files -f Tajik.lang Tajik
%defattr(644,root,root,755)

%files -f Ukrainian.lang Ukrainian
%defattr(644,root,root,755)
%{_mandir}/uk/man1/*.1*
%{_mandir}/uk/man6/*.6*
%{_mandir}/uk/man7/*.7*
%{_mandir}/uk/man8/*.8*

%files -f Urdu.lang Urdu
%defattr(644,root,root,755)

%files -f Uzbek.lang Uzbek
%defattr(644,root,root,755)

%files -f Uyghur.lang Uyghur
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
