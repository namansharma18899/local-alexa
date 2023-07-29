# Copyright 2020 CloudAudit.AI. All Rights Reserved.
from services.speech_to_text import Speech_to_text
from services.text_to_speech import Text_to_speech


class ServicePool:
    clients = {"stt": Speech_to_text, "tts": Text_to_speech}
    __instance = None
    __idle = dict()
    __used = dict()
    __max_pool_size = 0

    def __init__(self, max_pool_size):
        if ServicePool.__instance is not None:
            raise NotImplemented(
                "Cannot create a new instance, " "this is a singleton class."
            )
        ServicePool.__instance = self
        if max_pool_size is not None:
            ServicePool.__max_pool_size = max_pool_size
        for client in self.clients.values():
            self.__idle[client] = list()
            self.__used[client] = list()

    @staticmethod
    def get_pool_instance():
        if ServicePool.__instance is None:
            ServicePool.__instance = ServicePool()
        return ServicePool.__instance

    def get_service(self, client_type, used=True):
        try:
            client_type_obj = self.clients.get(client_type)
            if (
                len(self.__used.get(client_type_obj))
                + len(self.__idle.get(client_type_obj))
                >= self.__max_pool_size
            ):
                raise BufferError("POOL SIZE IS FULL")
            idle_client = self.get_idle_service(client_type)
            if idle_client:
                return idle_client
            instance = client_type_obj()
            if used:
                (self.__used.get(client_type_obj)).append(instance)
            else:
                (self.__idle.get(client_type_obj)).append(instance)
            return instance
        except Exception as e:
            raise e

    def get_idle_service(self, client_type):
        try:
            client_type_obj = self.clients.get(client_type)
            if client_type_obj is None:
                raise Exception("No such client as {}".format(client_type))
            if (
                self.__idle.get(client_type_obj)
                and len(self.__idle.get(client_type_obj)) > 0
            ):
                i = self.__idle.get(client_type_obj).pop(0)
                self.__used.get(client_type_obj).append(i)
                return i
            else:
                return None
        except Exception as e:
            raise e

    def release_service(self, instance):
        try:
            client_type = instance.__class__
            if client_type in self.__used:
                if instance in self.__used[client_type]:
                    instance.revoke_client()
                    self.__idle.get(client_type).append(instance)
                    self.__used.get(client_type).remove(instance)
                    return True
                else:
                    raise Exception("No such Instance present")
            else:
                raise Exception("No such client exists")
        except Exception as e:
            raise e

    def get_all_unused(self):
        return self.__idle.copy()

    def get_all_used(self):
        return self.__used.copy()

    def get_number_of_used(self):
        return len(self.__used)

    def get_number_of_unused(self):
        return len(self.__idle)

    def max_pool_size(self):
        return self.__max_pool_size
