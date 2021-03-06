# coding: utf-8

"""
	Copyright 2018 OSIsoft, LLC
	Licensed under the Apache License, Version 2.0 (the "License");
	you may not use this file except in compliance with the License.
	You may obtain a copy of the License at
	
	  <http://www.apache.org/licenses/LICENSE-2.0>
	
	Unless required by applicable law or agreed to in writing, software
	distributed under the License is distributed on an "AS IS" BASIS,
	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	See the License for the specific language governing permissions and
	limitations under the License.
"""
from pprint import pformat
from six import iteritems


class PIStreamUpdatesRegister(object):
	swagger_types = {
		'status': 'str',
		'source': 'str',
		'source_name': 'str',
		'source_path': 'str',
		'latest_marker': 'str',
		'exception': 'PIErrors',
	}

	attribute_map = {
		'status': 'Status',
		'source': 'Source',
		'source_name': 'SourceName',
		'source_path': 'SourcePath',
		'latest_marker': 'LatestMarker',
		'exception': 'Exception',
	}
	def __init__(self, status=None, source=None, source_name=None, source_path=None, latest_marker=None, exception=None):

		self._status = None
		self._source = None
		self._source_name = None
		self._source_path = None
		self._latest_marker = None
		self._exception = None

		if status is not None:
			self.status = status
		if source is not None:
			self.source = source
		if source_name is not None:
			self.source_name = source_name
		if source_path is not None:
			self.source_path = source_path
		if latest_marker is not None:
			self.latest_marker = latest_marker
		if exception is not None:
			self.exception = exception

	@property
	def status(self):
		return self._status

	@status.setter
	def status(self, status):
		self._status = status

	@property
	def source(self):
		return self._source

	@source.setter
	def source(self, source):
		self._source = source

	@property
	def source_name(self):
		return self._source_name

	@source_name.setter
	def source_name(self, source_name):
		self._source_name = source_name

	@property
	def source_path(self):
		return self._source_path

	@source_path.setter
	def source_path(self, source_path):
		self._source_path = source_path

	@property
	def latest_marker(self):
		return self._latest_marker

	@latest_marker.setter
	def latest_marker(self, latest_marker):
		self._latest_marker = latest_marker

	@property
	def exception(self):
		return self._exception

	@exception.setter
	def exception(self, exception):
		self._exception = exception

	def to_dict(self):
		result = {}
		for attr, _ in iteritems(self.swagger_types):
			value = getattr(self, attr)
			if isinstance(value, list):
				result[attr] = list(map(
					lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
					value
				))
			elif hasattr(value, "to_dict"):
				result[attr] = value.to_dict()
			elif isinstance(value, dict):
				result[attr] = dict(map(
					lambda item: (item[0], item[1].to_dict())
					if hasattr(item[1], "to_dict") else item,
					value.items()
				))
			else:
				result[attr] = value
		return result

	def to_str(self):
		return pformat(self.to_dict())

	def __repr__(self):
		return self.to_str()

	def __ne__(self, other):
		return not self == other

	def __eq__(self, other):
		if not isinstance(other, PIStreamUpdatesRegister):
			return False
		return self.__dict__ == other.__dict__

