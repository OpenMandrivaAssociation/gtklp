Summary: 	A GTK frontend for CUPS
Name: 		gtklp
Version: 	1.2.2
Release: 	%mkrel 2
License: 	GPL
Group: 		System/Configuration/Printing
Source0: 	http://prdownloads.sourceforge.net/gtklp/%{name}-%{version}.src.tar.bz2
Url: 		http://www.stud.uni-hannover.de/~sirtobi/gtklp/
Source1: 	gtklp-icon48.png
Source2: 	gtklp-icon32.png
Source3: 	gtklp-icon16.png
Patch0:		gtklp-1.2.2-simple.diff
BuildRequires: 	cups-common
BuildRequires:  gtk+2-devel
BuildPrereq: 	cups-devel > 1.1
Requires: 	cups > 1.1
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

%description
A GTK frontend for CUPS

%prep

%setup -q
%patch -p1

mkdir -p Mandriva
cp %{SOURCE1} Mandriva/gtklp-icon48.png
cp %{SOURCE2} Mandriva/gtklp-icon32.png
cp %{SOURCE3} Mandriva/gtklp-icon16.png

%build

%configure2_5x

%make

%install
rm -fr %{buildroot}

install -d %{buildroot}%{_menudir}
install -d %{buildroot}%{_liconsdir}
install -d %{buildroot}%{_iconsdir}
install -d %{buildroot}%{_miconsdir}

%makeinstall

# menu entry
cat > %{buildroot}%{_menudir}/%{name} <<EOF
?package(%{name}): \
needs="x11" \
section="Configuration/Printing" \
title="GTK CUPS" \
longtitle="GTK Frontend for CUPS" \
command="%{_bindir}/gtklp" \
icon="gtklp.png"
EOF

cat > %{buildroot}%{_menudir}/gtklpq <<EOF
?package(%{name}): \
needs="x11" \
section="Configuration/Printing" \
title="GTK Printer Queue" \
longtitle="GTK Frontend to GTKlp CUPS Queue" \
command="%{_bindir}/gtklpq" \
icon="gtklp.png"
EOF

# menu icon
install -m0644 Mandriva/gtklp-icon48.png %{buildroot}%{_liconsdir}/%{name}.png
install -m0644 Mandriva/gtklp-icon32.png %{buildroot}%{_iconsdir}/%{name}.png
install -m0644 Mandriva/gtklp-icon16.png %{buildroot}%{_miconsdir}/%{name}.png

# locales
%find_lang %name

%post 
%update_menus

%postun 
%clean_menus

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(0644,root,root)
%doc AUTHORS BUGS ChangeLog COPYING NEWS README TODO USAGE
%{_bindir}/*
%{_menudir}/*
%{_iconsdir}/*.png
%{_liconsdir}/*.png
%{_miconsdir}/*.png
%{_mandir}/man1/*
