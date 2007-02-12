Summary:	Removing image distorsions introduced by camera lenses
Summary(pl.UTF-8):   Usuwanie zniekształceń obrazu wprowadzonych przez obiektyw aparatu
Name:		clens
Version:	0.2
Release:	1
License:	GPL v2+
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/panotools/%{name}-%{version}.tar.gz
# Source0-md5:	d6edfce75bf555a08691d65fade7693d
Source1:	http://www.epaperpress.com/ptlens/download/PTLensProfiles.zip
# Source1-md5:	9144eaa751baf62408b69b77db0a52c7
URL:		http://panotools.sourceforge.net/
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
clens removes image distortions in JPEG images introduced by camera
lenses. clens is a Linux port of Thomas Niemann's PTLens for Windows
(<http://www.epaperpress.com/ptlens/>). Unlike PTLens, clens is a
command line program.

%description -l pl.UTF-8
clens służy do usuwania ze zdjęć w formacie JPEG zniekształceń obrazu
wprowadzonych przez obiektyw aparatu. clens to linuksowy port
windowsowego PTLens autorstwa Thomasa Niemanna
(<http://www.epaperpress.com/ptlens/>). W przeciwieństwie do PTLens
clens jest programem działającym z linii poleceń.

%prep
%setup -q
unzip -q %{SOURCE1} -d data

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install data/*.txt $RPM_BUILD_ROOT%{_datadir}/clens
mv -f data/README README.data
rm -rf $RPM_BUILD_ROOT{%{_prefix}/doc,%{_includedir},%{_datadir}/clens/README}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO README.data data/PTLensProfiles.pdf
%attr(755,root,root) %{_bindir}/clens
%{_datadir}/clens
%{_mandir}/man1/clens.1*
