Summary:	Tool that builds a chrooted environment
Summary(pl):	Narzêdzie tworz±ce ¶rodowisko w chroocie
Name:		jail
Version:	1.9a
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://www.jmcresearch.com/static/dwn/projects/jail/%{name}_%{version}.tar.gz
# Source0-md5:	06824a1255ce3da1bb86cb806bf15535
Patch0:		%{name}-install.patch
Requires(pre):  /usr/sbin/groupadd
Requires(postun):       /usr/sbin/groupdel
URL:		http://www.jmcresearch.com/projects/jail/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jail Chroot Project is an attempt of write a tool that builds a
chrooted environment. The main goal of Jail is to be as simple as
possible, and highly portable. The most difficult step when building a
chrooted environment is to set up the right libraries and files. Here,
Jail comes to the rescue with a tool to automagically configures &
builds all the required files, directories and libraries.

%description -l pl
Jail Chroot Project to próba napisania narzêdzia tworz±cego ¶rodowisko
w chroocie. G³ównym celem Jaila jest bycie tak prostym jak to tylko
mo¿liwe, a przy tym bardzo przeno¶nym. Najtrudniejszym krokiem przy
tworzeniu ¶rodowiska w chroocie jest w³a¶ciwe dobranie bibliotek i
plików. Tutaj z pomoc± przychodzi Jail z narzêdziem automatycznie
konfiguruj±cym i tworz±cym wszystkie wymagane pliki, katalogi i
biblioteki.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} -C src \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C src install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	SYSCONFDIR=%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%pre
        echo "Adding group jail GID=29."
        /usr/sbin/groupadd -g 29 jail

%postun
if [ "$1" = "0" ]; then
        echo "Removing group jail."
        %{_sbindir}/groupdel jail
fi

%files
%defattr(644,root,root,755)
%doc CHANGELOG README TODO
%attr(755,root,root) %{_bindir}/[!j]*
%attr(4750,root,jail) %{_bindir}/jail
%{_libdir}/jail
%attr(640,root,root) %verify(not size md5 mtime) %config(noreplace) %{_sysconfdir}/jail.conf
