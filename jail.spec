Summary:	Tool that builds a chrooted environment.
Name:		jail
Version:	1.9a
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://www.jmcresearch.com/static/dwn/projects/jail/%{name}_%{version}.tar.gz
# Source0-md5:	06824a1255ce3da1bb86cb806bf15535
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

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/jail

install jail $RPM_BUILD_ROOT%{_bindir}
install bin/addjailsw $RPM_BUILD_ROOT%{_bindir}
install bin/addjailuser $RPM_BUILD_ROOT%{_bindir}
install bin/mkjailenv $RPM_BUILD_ROOT%{_bindir}

install etc/jail.conf $RPM_BUILD_ROOT%{_sysconfdir}/jail/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README TODO
%attr(755,root,root) %{_bindir}/*
%attr(640,root,root) %verify(not size md5 mtime) %config(noreplace) %{_sysconfdir}/jail/jail.conf
