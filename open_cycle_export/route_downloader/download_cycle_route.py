from open_cycle_export.route_downloader.query_overpass import query_overpass


def download_cycle_route_data(search_area, cycle_network, route_number):

    query = """
        area["name"="{search_area}"]->.boundaryarea;
        (
            relation
                (area.boundaryarea)
                ["route"="bicycle"]
                ["network"="{cycle_network}"]
                ["ref"="{route_number}"];
            way(r);
        );
    """.format(
        search_area=search_area, cycle_network=cycle_network, route_number=route_number
    )

    # TODO: download relation metadata
    # way(r);
    # node(w);

    return query_overpass(query, "geom")


if __name__ == "__main__":
    download_cycle_route_data("England", "ncn", 22)