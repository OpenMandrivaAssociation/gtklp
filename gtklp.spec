Summary:	A GTK front-end for CUPS
Name:		gtklp
Version:	1.3.4
Release:	1
License:	GPLv2+
Group:		System/Configuration/Printing
Source0:	http://prdownloads.sourceforge.net/gtklp/%{name}-%{version}.src.tar.gz
Url:		http://gtklp.sourceforge.net/
Source1:	gtklp-icon48.png
Source2:	gtklp-icon32.png
Source3:	gtklp-icon16.png
Patch1:		gtklp-1.2.5-mdv-fix-str-fmt.patch
BuildRequires:	cups-common
BuildRequires:	cups-devel
BuildRequires:	pkgconfig(gtk+-2.0)
Requires:	cups

%description
A GTK front-end for CUPS.

%files -f %{name}.lang
%doc AUTHORS BUGS ChangeLog COPYING NEWS README TODO USAGE
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/*.png
%{_liconsdir}/*.png
%{_miconsdir}/*.png
%{_mandir}/man1/*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch1 -p1 -b .strfmt

sed -e '/DEF_BROWSER_CMD/{s:netscape:firefox:}' \
	-e '/DEF_HELP_HOME/{s:631/sum.html#STANDARD_OPTIONS:631/help/:}' \
	-i include/defaults.h

find . -perm 600 | xargs chmod 644

%build
autoreconf -fi
%configure --enable-forte
%make_build

%install
mkdir -p %{buildroot}/%{_datadir}/applications/
install -d %{buildroot}%{_liconsdir}
install -d %{buildroot}%{_iconsdir}
install -d %{buildroot}%{_miconsdir}

%make_install

# menu entry
cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Type=Application
Name=GTK CUPS
Comment=GTK Frontend for CUPS
Exec=%{_bindir}/gtklp
Icon=gtklp
Categories=HardwareSettings;Settings;GTK;
EOF

cat << EOF > %{buildroot}%{_datadir}/applications/gtklpq.desktop
[Desktop Entry]
Type=Application
Name=GTK Printer Queue
Comment=GTK Frontend to GTKlp CUPS Queue
Exec=%{_bindir}/gtklpq
Icon=gtklp
Categories=HardwareSettings;Settings;GTK;
EOF

# menu icon
install -m0644 %{SOURCE1} %{buildroot}%{_liconsdir}/%{name}.png
install -m0644 %{SOURCE2} %{buildroot}%{_iconsdir}/%{name}.png
install -m0644 %{SOURCE3} %{buildroot}%{_miconsdir}/%{name}.png

# locales
%find_lang %{name}

