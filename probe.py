    import requests
    import json

    def fetch_data(url: str):
        try:
            r = requests.get(url, timeout=5)

            r.raise_for_status()

            try:
                data = r.json()
            except ValueError:
                print("Not a valid JSON")
                return None

            if isinstance(data, list):
                names = [item.get("name") for item in data if isinstance(item, dict)]
                
                with open("names_new.json", "w", encoding="utf-8") as f:
                    json.dump(names, f, indent=2, ensure_ascii=False)
                print("JSON Names:", names)

            pretty = json.dumps(data, indent=2)
            print("Full JSON:", pretty)

            return data
        
        except requests.exceptions.Timeout:
            print("Request is Timed-out")

        except reqeusts.exceptions.RequestException as e:
            print(f"Request excpetion: {e}")
        return None