{ pkgs }: {
    deps = [
        pkgs.imagemagick6_light
        pkgs.python39Packages.pip
        pkgs.python310
        pkgs.bashInteractive
        pkgs.man
    ];
}