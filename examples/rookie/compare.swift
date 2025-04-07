// MARK: - Piwigo Server Methods    
    static func rotate(_ image: Image, by angle: Double,
                       completion: @escaping () -> Void,
                       failure: @escaping (NSError) -> Void) {
        // Prepare parameters for rotating image
        let paramsDict: [String : Any] = ["image_id"  : image.pwgID,
                                          "angle"     : angle,
                                          "pwg_token" : NetworkVars.pwgToken,
                                          "rotate_hd" : true]
        
        let JSONsession = PwgSession.shared
        JSONsession.postRequest(withMethod: pwgImageRotate, paramDict: paramsDict,
                                jsonObjectClientExpectsToReceive: ImageRotateJSON.self,
                                countOfBytesClientExpectsToReceive: 1000) { jsonData in
            // Decode the JSON if successful.
            do {
                // Decode the JSON into codable type ImageRotateJSON.
                let decoder = JSONDecoder()
                let uploadJSON = try decoder.decode(ImageRotateJSON.self, from: jsonData)
                
                // Piwigo error?
                if uploadJSON.errorCode != 0 {
                    let error = PwgSession.shared.localizedError(for: uploadJSON.errorCode,
                                                                 errorMessage: uploadJSON.errorMessage)
                    failure(error as NSError)
                    return
                }
                
                // Successful?
                if uploadJSON.result {
                    // Images rotated successfully ► Delete images in cache
                    image.deleteCachedFiles()
                    completion()
                }
                else {
                    // Could not delete images
                    failure(PwgSessionError.unexpectedError as NSError)
                }
            } catch {
                // Data cannot be digested
                let error = error as NSError
                failure(error)
            }
        } failure: { error in
            /// - Network communication errors
            /// - Returned JSON data is empty
            /// - Cannot decode data returned by Piwigo server
            failure(error)
        }
    }