Summary:	Tool that builds a chrooted environment.
Name:		jail
Version:	1.9a
Release:	0.1
License:	GPL
Group:		Applications/Communications
Source0:	http://www.jmcresearch.com/static/dwn/projects/jail/%{name}_%{version}.tar.gz
# Source0-md5:	06824a1255ce3da1bb86cb806bf15535
Patch0:		%{name}-Makefile.patch
URL:		http://www.jmcresearch.com/projects/jail/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jail Chroot Project is an attempt of write a tool that builds a
chrooted environment. The main goal of Jail is to be as simple as
possible, and highly portable. The most difficult step when building a
chrooted environment is to set up the right libraries and files. Here,
Jail comes to the rescue with a tool to automagically configures &
builds all the required files, directories and libraries.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_libdir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/jail

install {jail,bin/addjailsw,bin/addjailuser,bin/mkjailenv} $RPM_BUILD_ROOT%{_bindir}
install lib/libjail.pm $RPM_BUILD_ROOT%{_libdir}/
install etc/jail.conf $RPM_BUILD_ROOT%{_sysconfdir}/jail/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libjail.pm
%attr(640,root,root) %verify(not size md5 mtime) %config(noreplace) %{_sysconfdir}/jail/jail.conf
