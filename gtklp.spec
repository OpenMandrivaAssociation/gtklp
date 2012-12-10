Summary: 	A GTK frontend for CUPS
Name: 		gtklp
Version: 	1.2.8a
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

sed -e '/DEF_BROWSER_CMD/{s:netscape:firefox:}' \
        -e '/DEF_HELP_HOME/{s:631/sum.html#STANDARD_OPTIONS:631/help/:}' \
        -i include/defaults.h


mkdir -p Mandriva
cp %{SOURCE1} Mandriva/gtklp-icon48.png
cp %{SOURCE2} Mandriva/gtklp-icon32.png
cp %{SOURCE3} Mandriva/gtklp-icon16.png

%build
autoreconf -fi
%configure2_5x --enable-forte 

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


%changelog
* Sat Apr 28 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.8a-1mdv2012.0
+ Revision: 794268
- fix with broken link
- version update 1.2.8a

* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 1.2.8-1
+ Revision: 645233
- update to new version 1.2.8

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.7-2mdv2011.0
+ Revision: 610993
- rebuild

* Fri Dec 11 2009 Funda Wang <fwang@mandriva.org> 1.2.7-1mdv2010.1
+ Revision: 476418
- new version 1.2.7

* Wed Dec 09 2009 Jérôme Brenier <incubusss@mandriva.org> 1.2.5-5mdv2010.1
+ Revision: 475285
- number the Patch0 macro
- fix str fmt

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.2.5-4mdv2009.0
+ Revision: 246695
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sun Jan 27 2008 Funda Wang <fwang@mandriva.org> 1.2.5-2mdv2008.1
+ Revision: 158578
- add more category for desktop entry

* Sun Jan 27 2008 Funda Wang <fwang@mandriva.org> 1.2.5-1mdv2008.1
+ Revision: 158563
- update to new version 1.2.5

* Fri Jan 25 2008 Funda Wang <fwang@mandriva.org> 1.2.2-3mdv2008.1
+ Revision: 157807
- rebuild

* Thu Jan 03 2008 Thierry Vignaud <tv@mandriva.org> 1.2.2-2mdv2008.1
+ Revision: 141904
- auto-convert XDG menu entry
- s/BuildPrereq/BuildRequires/
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Austin Acton <austin@mandriva.org>
    - Import gtklp

