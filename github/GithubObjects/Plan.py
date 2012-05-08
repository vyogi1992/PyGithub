# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
# This allows None as a valid value for an optional parameter

class DefaultValueForOptionalParametersType:
    pass
DefaultValueForOptionalParameters = DefaultValueForOptionalParametersType()

class Plan( object ):
    def __init__( self, requester, attributes, lazy ):
        self.__requester = requester
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )
        if not lazy:
            self.__complete()

    @property
    def collaborators( self ):
        self.__completeIfNeeded( self.__collaborators )
        return self.__collaborators

    @property
    def name( self ):
        self.__completeIfNeeded( self.__name )
        return self.__name

    @property
    def private_repos( self ):
        self.__completeIfNeeded( self.__private_repos )
        return self.__private_repos

    @property
    def space( self ):
        self.__completeIfNeeded( self.__space )
        return self.__space

    def __initAttributes( self ):
        self.__collaborators = None
        self.__name = None
        self.__private_repos = None
        self.__space = None

    def __completeIfNeeded( self, testedAttribute ):
        if not self.__completed and testedAttribute is None:
            self.__complete()

    # @todo Do not generate __complete if type has no url attribute
    def __complete( self ):
        status, headers, data = self.__requester.request(
            "GET",
            self.__url,
            None,
            None
        )
        self.__useAttributes( data )
        self.__completed = True

    def __useAttributes( self, attributes ):
         #@todo No need to check if attribute is in attributes when attribute is mandatory
        if "collaborators" in attributes and attributes[ "collaborators" ] is not None:
            self.__collaborators = attributes[ "collaborators" ]
        if "name" in attributes and attributes[ "name" ] is not None:
            self.__name = attributes[ "name" ]
        if "private_repos" in attributes and attributes[ "private_repos" ] is not None:
            self.__private_repos = attributes[ "private_repos" ]
        if "space" in attributes and attributes[ "space" ] is not None:
            self.__space = attributes[ "space" ]
