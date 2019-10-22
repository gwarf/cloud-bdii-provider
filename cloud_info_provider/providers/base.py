import logging

from cloud_info_provider.providers import ssl_utils


class BaseProvider(object):
    def __init__(self, opts, **kwargs):
        self.opts = opts
        self.setup_logging()
        self._ca_info = {}

    def _get_endpoint_ca_information(self, url, **kwargs):
        if url not in self._ca_info:
            ca_info = ssl_utils.get_endpoint_ca_information(url, **kwargs)
            self._ca_info[url] = ca_info
        return self._ca_info[url]

    def get_site_info(self, **kwargs):
        return {}

    def get_images(self, **kwargs):
        return {}

    def get_templates(self, **kwargs):
        return {}

    def get_instances(self, **kwargs):
        return {}

    def get_compute_shares(self, **kwargs):
        return {}

    def get_compute_quotas(self, **kwargs):
        return {}

    def get_compute_endpoints(self, **kwargs):
        return {}

    def get_storage_endpoints(self, **kwargs):
        return {}

    @staticmethod
    def populate_parser(parser):
        '''Populate the argparser 'parser' with the needed options.'''

    def setup_logging(self):
        level = logging.DEBUG if self.opts.debug else logging.INFO
        logging.basicConfig(level=level)