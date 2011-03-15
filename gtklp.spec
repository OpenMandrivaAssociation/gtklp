Summary: 	A GTK frontend for CUPS
Name: 		gtklp
Version: 	1.2.8
Release: 	%mkrel 1
License: 	GPLv2+
Group: 		System/Configuration/Printing
Source0: 	http://prdownloads.sourceforge.net/gtklp/%{name}-%{version}.src.tar.gz
Url: 		http://gtklp.sourceforge.net/
Source1: 	gtklp-icon48.png
Source2: 	gtklp-icon32.png
Source3: 	gtklp-icon16.png
Patch0:		gtklp-1.2.7-simple.patch
Patch1:		gtklp-1.2.5-mdv-fix-str-fmt.patch
BuildRequires: 	cups-common
BuildRequires:  gtk+2-devel
BuildRequires: 	cups-devel > 1.1
Requires: 	cups > 1.1
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

%description
A GTK frontend for CUPS

%prep
%setup -q
%patch0 -p1 -b .simple
%patch1 -p1 -b .strfmt

mkdir -p Mandriva
cp %{SOURCE1} Mandriva/gtklp-icon48.png
cp %{SOURCE2} Mandriva/gtklp-icon32.png
cp %{SOURCE3} Mandriva/gtklp-icon16.png

%build
autoreconf -fi
%configure2_5x

%make

%install
rm -fr %{buildroot}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
install -d %{buildroot}%{_liconsdir}
install -d %{buildroot}%{_iconsdir}
install -d %{buildroot}%{_miconsdir}

%makeinstall_std

# menu entry
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Categories=HardwareSettings;Settings;GTK;
Name=GTK CUPS
Comment=GTK Frontend for CUPS
Exec=%{_bindir}/gtklp
Icon=gtklp
EOF

cat << EOF > %buildroot%{_datadir}/applications/mandriva-gtklpq.desktop
[Desktop Entry]
Type=Application
Categories=HardwareSettings;Settings;GTK;
Name=GTK Printer Queue
Comment=GTK Frontend to GTKlp CUPS Queue
Exec=%{_bindir}/gtklpq
Icon=gtklp
EOF

# menu icon
install -m0644 Mandriva/gtklp-icon48.png %{buildroot}%{_liconsdir}/%{name}.png
install -m0644 Mandriva/gtklp-icon32.png %{buildroot}%{_iconsdir}/%{name}.png
install -m0644 Mandriva/gtklp-icon16.png %{buildroot}%{_miconsdir}/%{name}.png

# locales
%find_lang %name

%if %mdkversion < 200900
%post 
%update_menus
%endif

%if %mdkversion < 200900
%postun 
%clean_menus
%endif

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(0644,root,root)
%doc AUTHORS BUGS ChangeLog COPYING NEWS README TODO USAGE
%{_bindir}/*
%{_datadir}/applications/mandriva-*.desktop
%{_iconsdir}/*.png
%{_liconsdir}/*.png
%{_miconsdir}/*.png
%{_mandir}/man1/*
