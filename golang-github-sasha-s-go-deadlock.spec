# https://github.com/sasha-s/go-deadlock
%global goipath github.com/sasha-s/go-deadlock
%global commit  d68e2bc52ae3291765881b9056f2c1527f245f1e
%global date    20180822

%gometa

Name:           golang-github-sasha-s-go-deadlock
Summary:        Online deadlock detection in go
Version:        0.2.0
Release:        8%{?dist}
License:        ASL 2.0

URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}


%package        devel
Summary:        %{summary}
BuildArch:      noarch

BuildRequires:  golang(github.com/petermattis/goid)

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup -p1


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc Readme.md


%changelog
* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.0-8.20180822gitd68e2bc
- Use forgeautosetup instead of gosetup.

* Sun Sep 02 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.0-7.20180822gitd68e2bc
- Bump to commit d68e2bc.
- Update to use spec 3.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.0-4
- Add another upstream patch to fix lock/unlock ordering.

* Fri Jun 01 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.0-3
- Add upstream patch to fix a potential race condition.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.0-1
- Update to version 0.2.0.

* Sat Dec 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0-1.20171130.git03d40e5
- Bump to commit 03d40e5.

* Tue Sep 05 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0-0.5.git565eb44
- Bump to commit 565eb44.

* Mon Aug 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0-0.4.git3410008
- Rebuild for golang(github.com/petermattis/goid) commit 0ded858.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.3.git3410008
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-0.2.git3410008
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 01 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0-0.1.git3410008
- First package for Fedora

